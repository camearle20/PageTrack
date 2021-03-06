#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.2 on Tue Apr 19 09:18:51 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

import serial.tools.list_ports

comList = []

try:
	comListRaw = list(serial.tools.list_ports.comports())
	for item in comListRaw:
		comList.append(item.device)
except:
	print "Error getting COM Port List, we will not populate the dropdown!"


# begin wxGlade: extracode
# end wxGlade




class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        #wx.Frame.__init__(self, *args, **kwds)
        #self.label_1 = wx.StaticText(self, wx.ID_ANY, "User ID: ")
        #self.userIDBox = wx.TextCtrl(self, wx.ID_ANY, "")
        #self.label_2 = wx.StaticText(self, wx.ID_ANY, "COM Port: ")
        #self.comPortBox = wx.ComboBox(self, wx.ID_ANY, choices=comList, style=wx.CB_DROPDOWN)
        #self.label_3 = wx.StaticText(self, wx.ID_ANY, "Server Address: ")
        #self.serverAddressBox = wx.TextCtrl(self, wx.ID_ANY, "")
        #self.label_4 = wx.StaticText(self, wx.ID_ANY, "Polling Interval (Seconds): ")
        #self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100)
        #self.label_5 = wx.StaticText(self, wx.ID_ANY, "Log Level: ")
        #self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=["Low", "Medium", "High", "Debug"], style=wx.CB_READONLY)
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "User ID: ")
        self.userIDBox = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_2 = wx.StaticText(self, wx.ID_ANY, "COM Port: ")
        self.comPortBox = wx.ComboBox(self, wx.ID_ANY, choices=comList, style=wx.CB_DROPDOWN)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, "Server Address: ")
        self.serverAddressBox = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_4 = wx.StaticText(self, wx.ID_ANY, "Polling Interval (Seconds): ")
        self.pollBox = wx.SpinCtrl(self, wx.ID_ANY, "", min=2, max=100)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, "Log Level: ")
        self.logBox = wx.ComboBox(self, wx.ID_ANY, choices=["low", "medium", "high", "debug"], style=wx.CB_READONLY)
        self.cancelButton = wx.Button(self, wx.ID_ANY, "Cancel")
        self.submitButton = wx.Button(self, wx.ID_ANY, "Submit")
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("PageTrack PC Config Editor")
        self.userIDBox.SetMinSize((222, 23))
        self.comPortBox.SetMinSize((222, 23))
        self.serverAddressBox.SetMinSize((222, 23))
        self.logBox.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(8, 4, 20, 20)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.userIDBox, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.comPortBox, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.serverAddressBox, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.pollBox, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.logBox, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.cancelButton, 0, 0, 0)
        grid_sizer_1.Add(self.submitButton, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MainFrame
