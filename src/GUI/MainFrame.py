'''
Created on Jun 4, 2010

@author: blaze
'''
import wx
import os
import Canvas
import AboutBox
from ToolBar import ToolBar


class MainFrame(wx.Frame):
    
    def __init__(self,parent=None,id=-1, title="Gamra", pos = wx.DefaultPosition,
                 size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, id, title,pos, size)
        
        #============= Creating statusbar
        self.CreateStatusBar()
        
        #============= Creating About Box
        self.About = AboutBox.AboutBox()
        
        #============= Setting Frame Icon
        self.Icon = wx.Icon(os.path.normpath("icons/icon256.png"), wx.BITMAP_TYPE_PNG)
        
        #============= Making Main Menu
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT,"E&xit", "Terminate the program")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT,"&About","More information about this program")
        
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")
        menuBar.Append(help_menu, "&Help")
        self.MenuBar = menuBar
        
        #=================================================
        #======= Making Main layout of the window ========
        #=================================================
        box = wx.BoxSizer(wx.VERTICAL)
        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()
        
        #=============== Creating Canvas =================
        canvas = Canvas.Canvas( self, size=wx.Size(1000,1000) )  
        box.Add(canvas, 20, wx.EXPAND)
          
        #=============== Creating Toolbar =================
        tb = ToolBar.ToolBar(self)
        #The second parameter to make the vertical resizing factor to Zero and 
        #make Horizontal factor resizable 
        box.Add(tb, 0, wx.EXPAND | wx.ALL)
        
        #====== TODO: the properties table
        panel2 = wx.Panel(self)
        panel2.SetBackgroundColour("RED")
        box.Add(panel2, 10, wx.EXPAND)
        
        
        #connecting functions with actions
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
                
    def OnExit(self, event):
        self.Close(True)
        
    def OnAbout(self, event):
        self.About.Show()