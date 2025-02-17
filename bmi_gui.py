import tkinter
import tkinter.messagebox

class BMICalculator:
    def __init__(self):
        self.main = tkinter.Tk() # create main window
        self.main.title('BMI Calculator')

        # frames
        self.top = tkinter.Frame(self.main)
        self.middle = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main)

        # top frame1
        self.height_label = tkinter.Label(self.top, text='Enter your height in metres: ')
        self.height_entry = tkinter.Entry(self.top)

        self.height_label.pack(side='left')
        self.height_entry.pack(side='right')

        # middle frame2
        self.weight_label = tkinter.Label(self.middle, text='Enter your weight in kilograms: ')
        self.weight_entry = tkinter.Entry(self.middle)

        self.weight_label.pack(side='left')
        self.weight_entry.pack(side='right')

        # bottom frame3
        self.calc_button = tkinter.Button(self.bottom, text='Calculate BMI', command=self.calculate_bmi)
        self.reset_button = tkinter.Button(self.bottom, text='Reset Form', command=self.reset_form)

        self.calc_button.pack(side='left')
        self.reset_button.pack(side='right')

        # pack frames
        self.top.pack()
        self.middle.pack()
        self.bottom.pack()

        # focus on height entry
        self.height_entry.focus_set()
        
        tkinter.mainloop() # call main loop

    # calculates bmi and shows results
    def calculate_bmi(self):
        self.height = self.height_entry.get()
        self.weight = self.weight_entry.get()

        try:
            if (float(self.height) or float(self.weight)) <= 0:
                raise ValueError
            else:
                self.height = float(self.height)
                self.weight = float(self.weight)
                self.bmi = round(self.weight/(self.height**2), 2)

                self.bmi_label.configure(text='BMI for ' + str(self.height) + 'm, ' + str(self.weight) + 'kg = ' + str(self.bmi))
                tkinter.messagebox.showinfo('Results', 'Your BMI is ' + str(self.bmi))
                self.reset_form()
                self.height_entry.focus_set()
        except ValueError:
            tkinter.messagebox.showerror('Invalid Input', 'Enter two positive numbers')
    
    def reset_form(self):
        self.height_entry.delete(0, tkinter.END)
        self.weight_entry.delete(0, tkinter.END)

        self.height_entry.focus_set()

gui = BMICalculator()
