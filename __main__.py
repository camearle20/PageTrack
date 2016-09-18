#
#PageTrack for PC v. 0.1 Alpha
#

#Import required libraries
import sys
import re
import pynmea2
import serial
import logging
import traceback
import thread
import time
import zmq
from zmq.log import handlers as zmqhandlers
import easygui
import __builtin__


#Configure logging
try:
    __builtin__.logger = logging.getLogger() #Create a logger, and share it across all modules with builtin
    logger.setLevel(logging.DEBUG) #Temporary
    fh = logging.FileHandler('main.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler() #Output the logged info to the STDOUT
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s') #Create our logging formatter
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh) #Add the handlers to the logger object
    logger.addHandler(ch)

    logger.info('Logger configured')
except:
    print "CRITICAL: Logger failed to configure"
    print "CRITICAL: Please verify your permissions settings"
    print "CRITICAL: Exiting!"
    sys.exit("Logger Failure")


#Configure socket
try:
    context = zmq.Context()
    sock = context.socket(zmq.PUB)
    sock.bind("tcp://127.0.0.1:5690") #Bind to a localhost socket
    sh = zmqhandlers.PUBHandler(sock) #Create a log handler for the socket so that the Control Panel can recieve errors
    sh.setLevel(logging.DEBUG)
    sh.root_topic = 'log'
    logger.addHandler(sh) #Add socket to the logger
    sockEnabled = True
    logger.info("Socket established")
except:
    sockEnabled = False
    logger.error("Error establishing ZeroMQ socket for Control Panel communication!")

def errorHandler(*exc_info): #Custom exception handling, for logging unhandled exceptions
    text = "".join(traceback.format_exception(*exc_info))
    logger.exception(text)
    sys.exit()

sys.excepthook = errorHandler #Set the exception handler to our own

time.sleep(2) #Give everything a chance to load before starting

#Import local modules
import config
import serialport
import networking


#Read configuration settings

configSettingsRaw = config.Config()
class ConfigSettingsDecoder: #We'll define a small class here to keep the config settings organized
    user = configSettingsRaw['user']
    port = configSettingsRaw['port']
    server = "http://"+configSettingsRaw['server']+"/lost.php" #Append protocol and script to the server address
    try:
        if float(configSettingsRaw['pollint']) < 1 or float(configSettingsRaw['pollint']) > 120:
            pollint = 10
        else:
            pollint = float(configSettingsRaw['pollint'])
    except:
        pollint = 10
    debuglevel = configSettingsRaw['debuglevel']

configSettings = ConfigSettingsDecoder() #Create an instance of our class where config settings will be stored

#Print data for debugging purposes
print configSettings.user
print configSettings.port
print configSettings.server
print configSettings.pollint
print configSettings.debuglevel

#Now that we have config settings, we can attempt to establish a serial link with the GPS device

#global device
#device = serialport.SerialPort(configSettings.port, 4800) #Call the serialport module to establish the connection, which returns a serialport instance



#Future Proofing

numSats = "0"
alt = "0"
lat = "0"
lon = "0"
spd = "0"
hed = "0"
acc = "10000"

sw = "n"

#Main program loop

def getData():

    #Predefine location variables to avoid errors when running multiple threads
    global numSats
    global alt
    global lat
    global lon
    global spd
    global hed
    global acc

    while True:
        try:
            line = device.readline()
        except:
            logger.error("GPS device lost")
            logger.critical("Serial device on port " + configSettings.port + " lost.  Attempting to re-establish")
            serialReconnect() #Program holds here, halting the entire thread until serial is reconnected
        try:
            if "GGA" in line:
                parsed = pynmea2.parse(line)
                numSats = str(parsed.num_sats)
                alt = str(parsed.altitude * 0.514) #Convert knots to m/s
                acc = getAcc(numSats, parsed.horizontal_dil, parsed.gps_qual) #Run formula to get accuracy
                #print "Number of sats: " + numSats
                #print "Altitude (meters): " + alt

            if "RMC" in line:
                parsed = pynmea2.parse(line)
                lat = str('%.6f' % parsed.latitude)
                lon = str('%.6f' % parsed.longitude)
                spd = str(parsed.spd_over_grnd)
                hed = str(parsed.true_course)
                if lat == 0 or lon == 0:
                    logger.warning("Invalid Coordinates")
                #print "Latitude: " + lat
                #print "Longitude: " + lon
                #print "Speed over Ground: " + spd
                #print "Heading: " + hed
        except:
            logger.warning("Unexpected NMEA data found, waiting for next read")

        #print "-----------------------------------"

        time.sleep(0.1) #Add a delay to prevent CPU throttling


def getAcc(numSats, hdop, qual):
    if qual == 0:
        accuracy = 10000
        logger.warning("Innacurate GPS Data")
    elif numSats < 4:
        accuracy = 300
        logger.warning("Innacurate GPS Data")
    elif numSats > 4:
        accuracy = 3 * float(hdop)
    else:
        accuracy = 300
        logger.warning("Invalid accuracy data recieved")
    return accuracy


def sendData():
    while True:
        time.sleep(configSettings.pollint)
        networking.MakeRequest(configSettings.server, acc, lat, lon, configSettings.user, sw, alt, spd, hed) #Send the data to the server
        networking.SendSocketReport(sock)

def sendCPData():
    while True:
        time.sleep(10)
        networking.SendSocket(sock, numSats, alt, lat, lon, spd, hed, acc) #Send the data to the Control Panel

def serialReconnect(): #This needs to halt the function, so we will throw in a while loop
    global device
    while True:
        time.sleep(10) #Prevent the lovely BSOD on the world's "most robust" OS
        retry = serialport.ReConnect(configSettings.port, 4800)
        if retry != False:
            del device
            device = retry
            logger.info("GPS module reconnected")
            break


device = serialport.SerialPort(configSettings.port, 4800) #Call the serialport module to establish the connection, which returns a serialport instance

try:
    thread.start_new_thread(getData, ()) #Start threads for each function
    thread.start_new_thread(sendData, ())
    if sockEnabled: #Only start this thread if the socket established correctly
        thread.start_new_thread(sendCPData, ())
except:
    logger.critical("Failed to start thread")
    logger.critical("The program will now exit")
    sys.exit("Threading Failure")


while True:
    try:
        time.sleep(1) #Keep the main thread alive
    except:
        if(not(device == None)):
                device.close()
                device = None
                logger.info("Disconnected serial device.")
        logger.info("End of program, exiting!")
        break

sys.exit()
