#
#PageTrack PC
#SerialPort Module
#

#Import required libraries
import serial
import sys

#Show status in console
logger.info('Serial port module loaded')


def SerialPort(comPort, baudRate, timeOut=10.0): #For consistency across modules, we have an extra "useless" function here
    serialInstance = __establishSerial(comPort, baudRate, timeOut)
    if serialInstance == False:
        logger.error("Error connecting to GPS unit")
        logger.critical("Serial port could not be established.  Make sure the config is correct, and that the device is connected properly.")
        logger.critical("The program will now terminate on error condition 1") #Kill the program here to prevent errors further in the code, plus it's useless without a GPS device
        sys.exit("Serial Device Error")
    else:
        logger.info('Serial port established on port ' + comPort)
        return serialInstance #Send the device instance back to the main code

def ReConnect(comPort, baudRate, timeOut=10.0):
    serialInstance = __establishSerial(comPort, baudRate, timeOut)
    if serialInstance == False:
        logger.debug("Error reconnecting serial port")
        return False
    else:
        logger.info('Serial port re-established on port ' + comPort)
        return serialInstance #Send the device instance back to the main code


def __establishSerial(comPort, baudRate, timeOut): #Take values in from config
    try:
        port = serial.Serial(comPort,baudrate=baudRate,timeout=timeOut)
        return port
    except:
        logger.critical("Error establishing serial port!")
        return False