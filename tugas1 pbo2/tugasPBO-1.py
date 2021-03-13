import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PBO-C | Rozin Hilmi | 192410101112", pos = wx.DefaultPosition, size = wx.Size( 703,652 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		self.HelloWX111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"HelloWX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HelloWX111.Wrap( -1 )

		self.HelloWX111.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer111.Add( self.HelloWX111, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer182 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer182.SetMinSize( wx.Size( -1,50 ) )
		self.labelNama11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNama11.Wrap( -1 )

		self.labelNama11.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer182.Add( self.labelNama11, 0, wx.ALL, 5 )

		self.namaValue1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u": Rozin Hilmi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaValue1.Wrap( -1 )

		gSizer182.Add( self.namaValue1, 0, wx.ALL, 5 )


		bSizer111.Add( gSizer182, 1, wx.EXPAND, 5 )

		gSizer1811 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer1811.SetMinSize( wx.Size( -1,-50 ) )
		self.labelNim1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelNim1.Wrap( -1 )

		self.labelNim1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1811.Add( self.labelNim1, 0, wx.ALL, 5 )

		self.nimValue1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u": 192410101112", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nimValue1.Wrap( -1 )

		gSizer1811.Add( self.nimValue1, 0, wx.ALL, 5 )


		bSizer111.Add( gSizer1811, 1, wx.EXPAND, 5 )


		bSizer311.Add( bSizer111, 1, wx.EXPAND, 5 )


		bSizer41.Add( bSizer311, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer41 )
		self.m_panel1.Layout()
		bSizer41.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALIGN_TOP|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )


	def __del__( self ):
		pass

app = wx.App()
frame1 = MyFrame1(parent=None)
frame1.Show()
app.MainLoop()