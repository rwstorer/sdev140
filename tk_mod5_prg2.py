import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint

class WindowOne(tk.Tk):
    def __init__(self):
        super().__init__()
        self.random_num: int = randint(1,100)
        self.title('Window One')
        self.geometry('640x480')
        self.label_entry: tk.Label = tk.Label(self,
                                         text='Label goes here')
        self.label_entry.place(x=5, y=5)
        self.data_entry: tk.Entry = tk.Entry(self, width=50)
        self.update()
        self.data_entry.place(x=self.label_entry.winfo_width()+10, y=5)
        self.update()
        self.btn_calc_state_tax: ttk.Button = ttk.Button(text='Check Answer',
                                                   command=lambda: self.check_answer())
        self.btn_calc_state_tax.place(x=440, y=3)
        self.update()
        
    def check_answer(self) -> None:
        entry: str = self.data_entry.get()
        # if statement to determine if the entry is correct
        # messagebox telling them if higher or lower or correct
        if self.random_num # rest of the if statement goes here
        messagebox.showinfo('State Tax',"message goes here")
    

window_one = WindowOne()
window_one.mainloop()    