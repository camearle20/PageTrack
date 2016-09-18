#
#PageTrack PC
#Networking module
#

#Import required libraries
import requests
import zmq


#Show status in console
logger.info("Networking module loaded")


def MakeRequest(server, acc, lat, lon, u, sw, alt, spd, hed):
    try:
        request = requests.post(server, json={'acc':str(acc), 'lat':str(lat), 'lon':str(lon), 'u':str(u), 'sw':str(sw), 'alt':str(alt), 'spd':str(spd), 'hed':str(hed)}) #Set up and make request
        print request.text #Print result from test server for debug
        logger.debug("Successfully made HTTP request to " + server)
    except:
        logger.error("Failed to send data to server")


def SendSocket(socket, numSats, alt, lat, lon, spd, hed, acc):

    #ORDER OF CONTROL PANEL DATA:
    # numSats, alt, lat, lon, spd, hed, acc
    #THIS ORDER MUST REMAIN CONSISTENT!

    cpData = "%s,%s,%s,%s,%s,%s,%s" % (str(numSats), str(alt), str(lat), str(lon), str(spd), str(hed), str(acc)) #Create a parsable string that can easily be split in C#
    try:
        socket.send_multipart(['data', cpData]) #Push the data to the socket
        logger.debug("Sent data over socket: " + cpData)
    except:
        logger.error("Error sending socket data!")


def SendSocketReport(socket):
    try:
        socket.send_multipart(['report', 'netsend'])
        logger.debug("Sent update report over socket")
    except:
        logger.error("Error sending socket data!")