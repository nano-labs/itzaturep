import wx
from datetime import datetime
from subprocess import call
from random import randint, choice

def capture():
    call(["streamer",
          "-f",
          "jpeg",
          "-o",
          "{}/trap_{}.jpeg".format("trapped",
                                   datetime.now().strftime("%Y%m%d_%H%M%S"))])
 
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Google Chrome - Gmail", size=(300,200))

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
        capture()
        images = ["trap1.jpg", "trap2.jpeg", "trap3.png", "trap4.jpg"]
        img = wx.Image(choice(images), wx.BITMAP_TYPE_ANY)
        pos = (randint(0, 1300), randint(0, 800))
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img), pos)
        self.panel.Refresh()
        # self.panel.BackgroundColour = wx.GREEN


if __name__ == '__main__':
    app = PhotoCtrl()
    app.MainLoop()

# app = wx.App(redirect=True)
# top = Frame()
# top.Show()
# app.MainLoop()