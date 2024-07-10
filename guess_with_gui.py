import tkinter
import tkinter.messagebox
from random import randint

"""
Too small, Too large, and Correct. 
When the game is over, you should disable these buttons 
and wait for the user to click New game, as before. 
"""

class WindowOne(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.randon_num: int = randint(1, 100)
        self.computer_guess: int = 1
        self.title('Guessing Game')
        self.geometry('640x480')
        self.lbl_msg = tkinter.Label(self, text='')
        self.lbl_msg.place(x=10, y=10)
        self.update()
        self.lbl_rnd_num = tkinter.Label(self, text=str(self.randon_num))
        self.lbl_rnd_num.place(x=20, y=300)
        self.update()
        self.btn_small = tkinter.Button(self,
            text='Too small', command=lambda: self.process_btn('Too small'))
        self.btn_small.place(x=10, y=100)
        self.update()
        self.btn_large = tkinter.Button(self,
            text='Too large', command=lambda: self.process_btn('Too large'))
        self.btn_large.place(x=75, y=100)
        self.update()
        self.btn_correct = tkinter.Button(self,
            text='Correct', command=lambda: self.process_btn('Correct'))
        self.btn_correct.place(x=150, y=100)
        self.update()
        self.btn_new_game = tkinter.Button(self,
            text='New game', command=lambda: self.process_btn('New game'))
        self.btn_new_game.place(x=300, y=100)
        self.update()
    
    def process_btn(self, btn_pressed: str):
        msg: str = ''
        if btn_pressed == 'Too small':
            self.computer_guess += 1 # computer guesses larger number
            msg = f"My new guess is: {self.computer_guess}"
        elif btn_pressed == 'Too large':
            self.computer_guess -= 1 # computer guesses smaller number
            msg = f"My new guess is: {self.computer_guess}"
        elif btn_pressed == 'Correct':
            msg = 'You guessed it!'
            self.btn_correct.configure(state='disabled')
            self.btn_small.configure(state='disabled')
            self.btn_large.configure(state='disabled')
        else:
            self.btn_correct.configure(state='normal')
            self.btn_small.configure(state='normal')
            self.btn_large.configure(state='normal')
            self.randon_num = randint(1, 100)
            msg = f"My guess is: {self.computer_guess}"
            self.lbl_rnd_num.configure(text=str(self.randon_num))
            
        self.lbl_msg.configure(text=msg)

window_one = WindowOne()
window_one.mainloop()