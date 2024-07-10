import tkinter

class WindowOne(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Window One')
        self.geometry('640x480')
        self.lbl_1 = tkinter.Label(text='Enter a Temperature and click the button to convert it:')
        self.lbl_1.place(x=5, y=5)
        self.update()
        self.entry_temp = tkinter.Entry(self, width=10)
        self.entry_temp.place(x=300, y=5)
        self.update()
        self.btn_f = tkinter.Button(text="Fahrenheit", command=lambda: self.proc_btn('F'))
        self.btn_f.place(x=10, y=200)
        self.update()
        self.btn_c = tkinter.Button(text="Celcius", command=lambda: self.proc_btn('C'))
        self.btn_c.place(x=150, y=200)
    
    def proc_btn(self, btn):
        if btn == 'F':
            # convert from celcius to farenheit
            # F = 9/5 * C + 32
            cel: int = int(self.entry_temp.get())
            far: str = str(9/5 * cel + 32)
            self.entry_temp.insert(0, far)
            self.entry_temp.delete(0,"END")
        else:
            pass
            # convert from farenheit to celcius
            # C = 5/9 * F - 32

window_one = WindowOne()
window_one.mainloop()