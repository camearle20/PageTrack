import wx
import os, sys
import ConfigParser
import easygui

import ConfigEditorGui

configPath = "config.cfg"

user = ""
port = "COM3"
server = "pgtrksrv01.net"
pollint = "10"
debuglevel = "Debug"

config = ConfigParser.ConfigParser({'user':user, 'port':port, 'server':server, 'pollint':pollint, 'debuglevel':debuglevel})


config.read(configPath)

def __createConfig():
    try:
        #Set config file options to the defined defaults
        config.set("DEFAULT", 'accuracy', accuracy)
        config.set("DEFAULT", 'user', user)
        config.set("DEFAULT", 'port', port)
        config.set("DEFAULT", 'server', server)
        config.set("DEFAULT", 'debuglevel', debuglevel)
        logger.info('Creating new config')
        with open(configPath, 'wb') as configFile: #Open/Create the file
            config.write(configFile) #Write the data
        return True
    except:
        return False
        
if not os.path.isfile(configPath):
    __createConfig() #If the config doesn't exist, create it, and then return here



user = config.get("DEFAULT", 'user')
port = config.get("DEFAULT", 'port')
server = config.get("DEFAULT", 'server')
pollint = config.get("DEFAULT", 'pollint')
debuglevel = config.get("DEFAULT", 'debuglevel')


def quit(e):
    sys.exit()
    
def submit(e):
    print "Running Submit"
    global user
    global port
    global server
    global pollint
    global debuglevel
    userNew = str(top.userIDBox.GetValue())
    portNew = str(top.comPortBox.GetValue())
    serverNew = str(top.serverAddressBox.GetValue())
    pollintNew = str(top.pollBox.GetValue())
    debuglevelNew = str(top.logBox.GetValue())
    errors = ""

    if not userNew:
        errors+="User ID cannot be blank\n"
    elif len(userNew) < 8:
        errors+="User ID must be greater than 8 characters\n"
    else:
        user = userNew

    if not portNew:
        errors+="COM Port cannot be blank\n"
    else:
        port = portNew

    if not serverNew:
        errors+="Server Address cannot be blank\n"
    else:
        server = serverNew

    if not pollintNew:
        errors+="Poll Interval cannot be blank\n"
    else:
        pollint = pollintNew

    if debuglevelNew:
        debuglevel = debuglevelNew

    if not errors:
        writeData(user ,port, server, pollint, debuglevel)
        sys.exit(0)
    else:
        easygui.msgbox(errors)
        return
    
    
def writeData(user, port, server, pollint, debuglevel):
    try:
        #Set config file options to the defined defaults
        config.set("DEFAULT", 'user', user)
        config.set("DEFAULT", 'port', port)
        config.set("DEFAULT", 'server', server)
        config.set("DEFAULT", 'pollint', pollint)
        config.set("DEFAULT", 'debuglevel', debuglevel)
        with open(configPath, 'wb') as configFile: #Open/Create the file
            config.write(configFile) #Write the data
    except:
        easygui.msgbox('Error setting up config, are your permissions set correctly?')
    
    
def showCurrent():
    try:
        top.userIDBox.SetValue(user)
        top.comPortBox.SetValue(port)
        top.serverAddressBox.SetValue(server)
        top.pollBox.SetValue(float(pollint))
        top.logBox.SetValue(debuglevel)
    except:
        pass

app = wx.App(False)
frame = wx.Frame(None)
style = wx.DEFAULT_FRAME_STYLE & (~wx.MAXIMIZE_BOX) & (~wx.RESIZE_BORDER)
top = ConfigEditorGui.MainFrame(frame, style=style)
top.cancelButton.Bind(wx.EVT_BUTTON, quit)
top.submitButton.Bind(wx.EVT_BUTTON, submit)
showCurrent()
top.Show()
app.MainLoop()












#                    xxxx                  xxxx
#                 x        x            x        x
#                x           x         x           x
#                     xx                    xx
#                   x    x                x    x
#                  x      x              x      x
#                  x      x              x      x
#                  x    xxx              x    xxx
#                  x   xxxx              x   xxxx
#                   x xxxx                x xxxx
#                    xxx         xxx       xxx
#                               x   x
#                               x   x
#                xx              xxx             xx
#              xx                                  xx
#            xxx                                    xxx
#               xx                                xx
#                 xx                             xx
#                   xxxx                      xxxx
#                        xxx               xxx
#                            xxxx     xxx

#	__________________            _______  _______  _        _______  _ 
#	\__   __/\__   __/  |\     /|(  ___  )(  ____ )| \    /\(  ____ \( )
#	   ) (      ) (     | )   ( || (   ) || (    )||  \  / /| (    \/| |
#	   | |      | |     | | _ | || |   | || (____)||  (_/ / | (_____ | |
#	   | |      | |     | |( )| || |   | ||     __)|   _ (  (_____  )| |
#	   | |      | |     | || || || |   | || (\ (   |  ( \ \       ) |(_)
#	___) (___   | |     | () () || (___) || ) \ \__|  /  \ \/\____) | _ 
#	\_______/   )_(     (_______)(_______)|/   \__/|_/    \/\_______)(_)

# (Excuse the ASCII art, but it works.)
