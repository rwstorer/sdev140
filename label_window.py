import tkinter
import tkinter.messagebox

class WindowOne(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Window One')
        self.geometry('640x480')
        self.img = tkinter.PhotoImage(file='down_button.png')
        self.configure(bg='purple')
        self.img_label = tkinter.Label(self, image=self.img)
        self.img_label.place(x=0, y=0, relheight=1, relwidth=1)
        self.update()
        self.label_entry = tkinter.Label(self,
                                         text='Label goes here',
                                         fg='yellow',bg='MediumPurple4')
        self.label_entry.place(x=5, y=5)
        self.update()
        self.edit_box = tkinter.Entry(self, width=10)
        self.edit_box.place(x=100, y=5)
        self.update()
        self.btn = tkinter.Button(text='Ok', 
            command=lambda: tkinter.messagebox.showinfo(title='OK', message='Button pressed'))
        self.btn.place(x=200, y=300)
        self.update()
        
    

window_one: WindowOne = WindowOne()
window_one.mainloop()
