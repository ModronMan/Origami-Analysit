######-IMPORT MODULES-##################################################################################################
import wx               # IMPORT wxPYTHON
from Beveridge_Barran_plot_v2 import * # IMPORT CCSB CALCULATOR
#####-INITIALISE WINDOW-################################################################################################
#####-CREATES THE FRAME-################################################################################################
class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass,self).__init__(None, -1, 'ORIGAMI ANALYST/FRAMEWORK',
                                         size=(500, 500))
        self.basicGUI()
#######-GUI PANEL-######################################################################################################
    def basicGUI(self):
        panel = wx.Panel(self)
        self.SetBackgroundColour('#154360')
        self.SetTitle('ORIGAMI ANALYST/FRAMEWORK')
        self.Show(True)
#######-GUI LAYOUT AND DESIGN-##########################################################################################
        """THIS PART OF CODE IS RESPONSIBLE FOR THE LAYOUT AND DESIGN
         OF THE GUI, THIS INCLUDES ALL TEXT, COLORS AND BUTTONS"""
#######-TITLE TEXT-#####################################################################################################
        """TITLE OF PROGRAM IN WHITE"""
        title = wx.StaticText(panel, -1, 'Beveridge-Barran Plot', (10, 10))
        title.SetForegroundColour('#D0D3D4')  # hex color code
        title.SetBackgroundColour('#154360')
        font1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title.SetFont(font1)
#######-PROTEIN NAME TEXT-##############################################################################################
        name = wx.StaticText(panel, -1, 'Protein Name :', (10,40))
        name.SetForegroundColour('#D0D3D4')
        name.SetBackgroundColour('#154360')
        name.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.name = wx.TextCtrl(panel, pos=(170, 40), size=(100, 25))
#######-PROTEIN MASS TEXT-##############################################################################################
        mass = wx.StaticText(panel, -1, 'Protein Mass :', (10, 70))
        mass.SetForegroundColour('#D0D3D4')
        mass.SetBackgroundColour('#154360')
        mass.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.mass = wx.TextCtrl(panel, pos=(170, 70), size=(100, 25))
#######-LOWEST Z TEXT-##################################################################################################
        low_z = wx.StaticText(panel, -1, 'Lowest Charge State :', (10, 100))
        low_z.SetForegroundColour('#D0D3D4')
        low_z.SetBackgroundColour('154360')
        low_z.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.low = wx.TextCtrl(panel, pos=(240, 100), size=(100, 25))
#######-HIGHEST Z TEXT-#################################################################################################
        high_z = wx.StaticText(panel, -1, 'Highest Charge State :', (10, 130))
        high_z.SetForegroundColour('#D0D3D4')
        high_z.SetBackgroundColour('154360')
        high_z.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.high = wx.TextCtrl(panel, pos=(240, 130), size=(100, 25))
#######-SMALLEST CCS TEXT-##############################################################################################
        small = wx.StaticText(panel, -1, 'Smallest CCS :', (10, 160))
        small.SetForegroundColour('#D0D3D4')
        small.SetBackgroundColour('#154360')
        small.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.small = wx.TextCtrl(panel, pos=(170, 160), size=(100, 25))
#######-LARGEST CCS TEXT-###############################################################################################
        large = wx.StaticText(panel, -1, 'Largest CCS :', (10, 190))
        large.SetForegroundColour('#D0D3D4')
        large.SetBackgroundColour('#154360')
        large.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.large = wx.TextCtrl(panel, pos=(170, 190), size=(100, 25))
#######-BUTTON-#########################################################################################################
        Butttonplot = wx.Button(panel, -1, 'Plot', pos=(10, 210))
        Butttonplot.Bind(wx.EVT_BUTTON, self.OnPlot)
###-FUNCTIONS-##########################################################################################################
########################### PLOT BEVERIDGE-BARRAN ######################################################################
    def OnPlot(self, event):
        name = self.name.GetValue()
        mass = int(self.mass.GetValue())
        low = int(self.low.GetValue())
        high = int(self.high.GetValue())
        small = int(self.small.GetValue())
        large = int(self.large.GetValue())
        plot_Z(ORDDICT, DISDICT, get_input(name, mass, low, high, small, large)), plot_CCS(ORDDICT, DISDICT, get_input(name, mass, low, high, small, large))
#########################MAINLOOP#######################################################################################
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()
########################################################################################################################
main()
########################################################################################################################