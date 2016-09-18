#
#PageTrack PC
#Config Module
#


logger.info("Config module loaded")

configPath="config.cfg"

#Import required libraries
import ConfigParser
import os


#Default values

user = ""
port = "COM3"
server = "pgtrksrv01.net"
pollint = "10"
debuglevel = "high"

config = ConfigParser.ConfigParser({'user':user,'port':port,'server':server,'pollint':pollint,'debuglevel':debuglevel}) #Initialize config parser with defaults

def Config():
    return __readConfig()


#Check for config file

def __readConfig():
    #First, we'll check if the config exists
    logger.info('Reading config')
    config.read(configPath) #This works whether the config file exists or not
    if not os.path.isfile(configPath):
        logger.info('No configuration found, attempting to create one with defaults')
        if __createConfig(): #If the config doesn't exist, create it, and then return here
            logger.info('Data successfully written')
        else:
            logger.warning('Using default values')
        #Now we read the config, or it is empty we use the defaults
    user = config.get("DEFAULT", 'user')
    port = config.get("DEFAULT", 'port')
    server = config.get("DEFAULT", 'server')
    pollint = config.get("DEFAULT", 'pollint')
    debuglevel = config.get("DEFAULT", 'debuglevel')
    logger.info('Done grabbing values')
    return {'user':user,'port':port,'server':server,'pollint':pollint,'debuglevel':debuglevel}



def __createConfig():
    try:
        #Set config file options to the defined defaults
        config.set("DEFAULT", 'user', user)
        config.set("DEFAULT", 'port', port)
        config.set("DEFAULT", 'server', server)
        config.set("DEFAULT", 'pollint', pollint)
        config.set("DEFAULT", 'debuglevel', debuglevel)
        logger.info('Creating new config')
        with open(configPath, 'wb') as configFile: #Open/Create the file
            config.write(configFile) #Write the data
        return True
    except:
        logger.error('Error creating new config, are your permissions set correctly?')
        return False