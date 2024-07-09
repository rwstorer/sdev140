import tkinter

class WindowOne(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Window One')
        self.geometry('640x480')
        self.label_entry = tkinter.Label(self,
                                         text='Label goes here')
        self.label_entry.place(x=5, y=5)
        self.update()
        self.edit_box = tkinter.Entry(self, width=10)
        self.edit_box.place(x=100, y=5)
        self.update()
        
    

window_one: WindowOne = WindowOne()
window_one.mainloop()
