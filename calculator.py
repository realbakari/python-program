"""
Created on Mon Sept 26, 2019

Problem:
The calculator will be simpler than a normal calculator. The user should input 2
numbers into the 2 text boxes and then choose an operation to perform. The
result should be output somewhere on the GUI. If the user has not entered 2 
numbers, the buttons should display the appropriate error.

@author: Bakari Mustafa
"""

import wx


class Calculator(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.last_button_pressed = None
        self.display()

    def display(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL) # Main vertical sizer
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)

        self.solution = wx.TextCtrl(self, style=wx.TE_RIGHT)
        self.solution.SetFont(font)
        self.solution.Disable()
        main_sizer.Add(self.solution, 0, wx.expand|wx.ALL, 5)
        self.running_total = wx.StaticText(self)
        main_sizer.Add(self.running_total, 0, wx.ALIGN_RIGHT) # Add to main sizer
        
        # [7][8][9][/] 
        # [4][5][6][*]
        # [1][2][3][-]
        # [0][.][C][+]

        buttons = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['.', '0', '', '+']]
        for label_list in buttons:
            btn_sizer = wx.BoxSizer()
            for label in label_list:
                button = wx.Button(self, label=label)
                btn_sizer.Add(button, 1, wx.ALIGN_CENTER|wx.expand, 0)
                button.Bind(wx.EVT_BUTTON, self.update_equation)
            main_sizer.Add(btn_sizer, 1, wx.ALIGN_CENTER|wx.expand)

        equals_btn = wx.Button(self, label='=') # Calculate
        equals_btn.Bind(wx.EVT_BUTTON, self.on_total)
        main_sizer.Add(equals_btn, 0, wx.expand|wx.ALL, 3)

        clear_btn = wx.Button(self, label='Clear') # Clear
        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear)
        main_sizer.Add(clear_btn, 0, wx.expand|wx.ALL, 3)
        
        # Set sizer and center
        self.SetSizer(main_sizer)

    def equation(self, event):
        operators = ['/', '*', '-', '+']
        btn = event.GetEventObject()
        label = btn.GetLabel()
        current_equation = self.solution.GetValue()

        if label not in operators:
            if self.last_button_pressed in operators:
                self.solution.SetValue(current_equation + ' ' + label)
            else:
                self.solution.SetValue(current_equation + label)
        elif label in operators and current_equation != '' \
             and self.last_button_pressed not in operators:
            self.solution.SetValue(current_equation + ' ' + label)

        self.last_button_pressed = label

        for item in operators:
            if item in self.solution.GetValue():
                self.update_solution()
                break

    def update_solution(self):
        try:
            current_solution = str(eval(self.solution.GetValue()))
            self.running_total.SetLabel(current_solution)
            self.Layout()
            
             # Calculate result
            return current_solution
        
        # Show result
        except ZeroDivisionError:
            self.solution.SetValue('ZeroDivisionError')
        except:
            pass

    def on_clear(self, event):
        self.solution.Clear()
        self.running_total.SetLabel('')

    def on_total(self, event):
        solution = self.update_solution()
        if solution:
            self.solution.SetValue(solution)
            self.running_total.SetLabel('')

class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(
            None, title="Calculator",
            size=(350, 375))
        panel = Calculator(self)
        
        # put the panel on -- in a sizer to give it some space
        self.SetSizeHints(350, 375, 350, 375)
        self.Show()


if __name__ == '__main__':
    # Run the application
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()