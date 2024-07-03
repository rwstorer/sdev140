import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class WindowOne(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Window One')
        self.geometry('640x480')
        self.label_entry: tk.Label = tk.Label(self,
                                         text='Label goes here')
        self.label_entry.place(x=5, y=5)
        self.data_entry: tk.Entry = tk.Entry(self, width=50)
        self.update()
        self.data_entry.place(x=self.label_entry.winfo_width()+10, y=5)
        self.update()
        self.btn_calc_state_tax: ttk.Button = ttk.Button(text='Calc Tax',
                                                   command=lambda: self.calc_state_tax())
        self.btn_calc_state_tax.place(x=440, y=3)
        self.update()
        
    def calc_state_tax(self) -> None:
        entry: str = self.data_entry.get()
        STATE_TAX_RATE: float = 0.025
        messagebox.showinfo('State Tax',str(float(entry) * STATE_TAX_RATE))
    
    def calc_couty_tax(self) -> None:
        # calculate
        # display the messagebox
        pass
        
    def calc_total_tax(self) -> None:
        # calculate
        # display the messagebox
        pass

window_one = WindowOne()
window_one.mainloop()    