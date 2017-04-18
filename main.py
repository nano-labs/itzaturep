import wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Hello World", size=(300,200))

class PhotoCtrl(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = Frame()
        self.panel = wx.Panel(self.frame)
        self.panel.Bind(wx.EVT_LEFT_UP, self.onClick)
        img = wx.Image("print.png", wx.BITMAP_TYPE_ANY)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img))
        self.imageCtrl.Bind(wx.EVT_LEFT_UP, self.onClick)
        self.frame.Show()


    def onClick(self, event):
        print("click")
        img = wx.Image("trap.jpg", wx.BITMAP_TYPE_ANY)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img), (200, 200))
        self.panel.Refresh()
        # self.panel.BackgroundColour = wx.GREEN


if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()

# app = wx.App(redirect=True)
# top = Frame()
# top.Show()
# app.MainLoop()