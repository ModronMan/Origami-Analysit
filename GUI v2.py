######-IMPORT MODULES-##################################################################################################
import os               # IMPORT OPERATING SYSTEM
import wx               # IMPORT wxPYTHON
from CCSB_v2_1 import * # IMPORT CCSB CALCULATOR
#####-INITIALISE WINDOW-################################################################################################
#####-CREATES THE FRAME-################################################################################################
class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass,self).__init__(None, -1, 'ORIGAMI ANALYST/FRAMEWORK',
                                         size=(500, 250))
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
        title = wx.StaticText(panel, -1, 'Collision Cross Section Boundary Calculation', (10, 10))
        title.SetForegroundColour('#D0D3D4')  # hex color code
        title.SetBackgroundColour('#154360')
        font1 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title.SetFont(font1)
#######-AMINO ACID SEQUENCE TEXT-#######################################################################################
        AAS = wx.StaticText(panel, -1, 'Sequence:', (10, 50))
        AAS.SetForegroundColour('#D0D3D4')  # hex color code
        AAS.SetBackgroundColour('#154360')
        AAS.SetFont(font1)
#######-COMPACT OUTPUT TEXT-############################################################################################
        comp = wx.StaticText(panel, -1, 'Compact (\u212B\u00B2 )  = ', (10, 150))
        comp.SetForegroundColour('#D0D3D4')
        comp.SetFont(font1)
#######-EXTENDED OUTPUT TEXT-###########################################################################################
        extend = wx.StaticText(panel, -1, 'Extended (\u212B\u00B2 ) = ', (10, 180))
        extend.SetForegroundColour('#D0D3D4')
        extend.SetFont(font1)
#######-TEXT BOX-#######################################################################################################
        self.seq = wx.TextCtrl(panel, pos=(150, 50), size=(300, 25))
        #BUTTON
        Button1 = wx.Button(panel, -1, 'IMPORT', pos=(10, 80), size=(100, 25))
        Button1.Bind(wx.EVT_BUTTON, self.OnImport)
        Button2 = wx.Button(panel, -1, 'CALCULATE', pos=(10, 110), size=(100, 25))
        Button2.Bind(wx.EVT_BUTTON, self.OnCalculate)
        #COMPACT RESULT TEXT BOX
        self.compact = wx.StaticText(panel, label='', pos=(180, 150))
        self.compact.SetForegroundColour('#D0D3D4')
        self.compact.SetBackgroundColour('#154360')
        self.compact.SetFont(font1)
        #EXTENDED RESULT TEXT BOX
        self.extended = wx.StaticText(panel, label='', pos=(180, 180))
        self.extended.SetForegroundColour('#D0D3D4')
        self.extended.SetBackgroundColour('#154360')
        self.extended.SetFont(font1)
###-FUNCTIONS-##########################################################################################################
############################ IMPORT AMINO ACID SEQUENCE ################################################################
    def OnImport(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as fobj:
                for line in fobj:
                    self.seq.WriteText(line)
########################## CALCULATE CCSB ##############################################################################
    def OnCalculate(self, event):
        sequence = self.seq.GetValue()
        sequence = list(sequence)
        for i in sequence:
            if i == '\n':
                sequence.remove(i)
        high = high_scaling(sequence)
        high = round(high, 2)
        high = str(high)
        low = low_scaling(sequence)
        low = round(low, 2)
        low = str(low)
        self.extended.SetLabel(high)
        self.compact.SetLabel(low)
#########################MAINLOOP#######################################################################################
def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()
########################################################################################################################
main()
########################################################################################################################