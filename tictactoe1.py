from tkinter import *
from threading import Thread
from tkinter import messagebox
import time, random

class App(Tk):
    is_won = True
    value = []

    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.geometry('470x265')
        self.turn = 'X'

        # game frame
        self.game_frame = Frame(self, bg='white')
        self.game_frame.place(relx=.0, rely=.0, relwidth=.5, relheight=1)

        #button
        self.btn1 = Button(self.game_frame, text='', command=lambda :self.onclick(1), height=2, width=4, font='time 20 bold')
        self.btn1.grid(column=0, row=0)

        self.btn2 = Button(self.game_frame, text='',  command=lambda :self.onclick(2),  height=2, width=4, font='time 20 bold')
        self.btn2.grid(column=1, row=0)

        self.btn3 = Button(self.game_frame, text='',  command=lambda :self.onclick(3), height=2, width=4, font='time 20 bold')
        self.btn3.grid(column=2, row=0)

        self.btn4 = Button(self.game_frame, text='',  command=lambda :self.onclick(4), height=2, width=4, font='time 20 bold')
        self.btn4.grid(column=0, row=1)

        self.btn5 = Button(self.game_frame, text='',  command=lambda :self.onclick(5), height=2, width=4, font='time 20 bold')
        self.btn5.grid(column=1, row=1)

        self.btn6 = Button(self.game_frame, text='',  command=lambda :self.onclick(6), height=2, width=4, font='time 20 bold')
        self.btn6.grid(column=2, row=1)

        self.btn7 = Button(self.game_frame, text='',  command=lambda :self.onclick(7), height=2, width=4, font='time 20 bold')
        self.btn7.grid(column=0, row=2)

        self.btn8 = Button(self.game_frame, text='',  command=lambda :self.onclick(8), height=2, width=4, font='time 20 bold')
        self.btn8.grid(column=1, row=2)

        self.btn9 = Button(self.game_frame, text='',  command=lambda :self.onclick(9), height=2, width=4, font='time 20 bold')
        self.btn9.grid(column=2, row=2)

        #output frame
        self.output = Frame(self, bg='black')
        self.output.place(relx=.5, rely=.2, relwidth=.5, relheight=1)

        #response of turn check box
        self.turn_box = Label(self, bg='black', fg='green', font=20, justify=CENTER)
        self.turn_box.place(relx=.5, rely=.2, relwidth=.4, relheight=.1)

        # turn label x
        self.check_box1 = IntVar()
        self.x_label = Checkbutton(self, variable=self.check_box1, text='X-player')
        self.x_label.place(relx=.5)
        # turn label o
        self.check_box2 = IntVar()
        self.o_label = Checkbutton(self, variable=self.check_box2, text='O-player')
        self.o_label.place(relx=.7)

        # computer check box
        self.computer_box = IntVar()
        self.computer_label = Checkbutton(self, variable=self.computer_box, text='Play with computer.', fg='red')
        self.computer_label.place(relx=.5, rely=.1)

        # static name of o and x point
        static_x = Label(self, bg='black', text='X - points =>', font=30, fg='green', anchor='nw', justify=CENTER)
        static_x.place(relx=.5, rely=.4, relwidth=.2, relheight=.1)
        static_o = Label(self, bg='black', text='O - points =>', fg='green', font=30, anchor='nw', justify=CENTER)
        static_o.place(relx=.5, rely=.7, relwidth=.2, relheight=.1)

        # dynamic x and o points
        self.x_points = Label(self, bg='black', fg='red',text='0', font=30, anchor='nw', justify=CENTER)
        self.x_points.place(relx=.7, rely=.4, relwidth=.1, relheight=.1)

        self.o_points = Label(self, bg='black',text='0', fg='red', font=30, anchor='nw', justify=CENTER)
        self.o_points.place(relx=.7, rely=.7, relwidth=.1, relheight=.1)

    def erase_after(self):
        self.btn1['text'] = ''
        self.btn2['text'] = ''
        self.btn3['text'] = ''
        self.btn4['text'] = ''
        self.btn5['text'] = ''
        self.btn6['text'] = ''
        self.btn7['text'] = ''
        self.btn8['text'] = ''
        self.btn9['text'] = ''

    def onclick(self, args):
        def turn_choice():
            if self.computer_box.get() == 0 and (self.check_box1.get() == 1 or self.check_box2.get() == 1):
                if self.turn=='X':
                    self.turn='O'
                else: self.turn = 'X'

        turn_choice()

        if self.check_box2.get() == self.check_box1.get() == self.computer_box.get():
            self.turn_box['text'] = 'Select one player!'
            def rub(text):
                time.sleep(2)
                self.turn_box['text'] = text
            Thread(target=rub, args=('',)).start()

        elif self.is_won and (self.check_box2.get()==1 or self.check_box1.get()==1):
            if self.btn1['text'] == '' and args==1: self.btn1['text'] = self.turn
            elif self.btn2['text'] == '' and args==2: self.btn2['text'] = self.turn
            elif self.btn3['text'] == '' and args==3: self.btn3['text'] = self.turn
            elif self.btn4['text'] == '' and args==4: self.btn4['text'] = self.turn
            elif self.btn5['text'] == '' and args==5: self.btn5['text'] = self.turn
            elif self.btn6['text'] == '' and args==6: self.btn6['text'] = self.turn
            elif self.btn7['text'] == '' and args == 7: self.btn7['text'] = self.turn
            elif self.btn8['text'] == '' and args == 8: self.btn8['text'] = self.turn
            elif self.btn9['text'] == '' and args == 9: self.btn9['text'] = self.turn

            # grab all data
            self.value = [self.btn1['text'], self.btn2['text'], self.btn3['text'], self.btn4['text'], self.btn5['text'],
                         self.btn6['text'], self.btn7['text'], self.btn8['text'], self.btn9['text']]

            Thread(target=self.all_call, args=(self.value,)).start()

    def all_call(self, value):
        # computer player
        computer_thread = Thread(target=self.computer, args=(value,))
        computer_thread.start()

        # winning calculator
        winner_thread = Thread(target=self.winner_checker, args=(self.turn_box, value,))
        winner_thread.start()

        # this for tie checker
        tie_thread = Thread(target=self.tie_checker, args=(value,))
        tie_thread.start()

    def winner_checker(self, turn_box, btn_value):
        check1 = self.btn1['text'] == self.btn2['text'] == self.btn3['text'] != ''
        check2 = self.btn4['text'] == self.btn5['text'] == self.btn6['text'] != ''
        check3 = self.btn7['text'] == self.btn8['text'] == self.btn9['text'] != ''

        check4 = self.btn1['text'] == self.btn4['text'] == self.btn7['text'] != ''
        check5 = self.btn2['text'] == self.btn5['text'] == self.btn8['text'] != ''
        check6 = self.btn3['text'] == self.btn6['text'] == self.btn9['text'] != ''

        check7 = self.btn1['text'] == self.btn5['text'] == self.btn9['text'] != ''
        check8 = self.btn3['text'] == self.btn5['text'] == self.btn7['text'] != ''

        def add_points(value):
            o = self.o_points['text']
            x = self.x_points['text']
            win_x = str(int(x)+10)
            win_o = str(int(o)+10)
            if check1:
                if 'O' in [self.btn1['text'] , self.btn2['text'] ,self.btn3['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check2:
                if 'O' in [self.btn4['text'], self.btn5['text'], self.btn6['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check3:
                if 'O' in [self.btn7['text'], self.btn8['text'], self.btn9['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check4:
                if 'O' in [self.btn1['text'], self.btn4['text'], self.btn7['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check5:
                if 'O' in [self.btn2['text'], self.btn5['text'], self.btn8['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check6:
                if 'O' in [self.btn3['text'], self.btn6['text'], self.btn9['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check7:
                if 'O' in [self.btn1['text'], self.btn5['text'], self.btn9['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x
            elif check8:
                if 'O' in [self.btn3['text'], self.btn5['text'], self.btn7['text']]:
                    self.o_points['text'] = win_o
                else: self.x_points['text'] = win_x




        if self.is_won:
            if check1:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check2:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check3:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check4:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check5:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check6:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check7:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()
            elif check8:
                turn_box['text']='Congratulation, You Won.'
                messagebox.showinfo('Tic-Tac-Toe', 'Wins!')
                add_points(btn_value)
                self.erase_after()

        Thread(target=self.tie_checker, args=(self.value,)).start()

    def tie_checker(self, check):
        if self.is_won:
            if ('X' in check) and ('O' in check) and ('' not in check):
                messagebox.showinfo('Tic-Tac-Toe', 'Tie!')
                self.erase_after()

    def computer(self, value):
        if self.computer_box.get()==1 and (self.check_box2.get()!=self.check_box1.get()):
            comp_turn = ''
            if True:
                if self.turn=='X': comp_turn = 'O'
                else: comp_turn = 'X'

            if (value[0] == value[1] != '') and value[2] == '': self.btn3['text'] = comp_turn
            elif (value[1] == value[2] != '') and value[0] == '': self.btn1['text'] = comp_turn
            elif (value[0] == value[2] != '') and value[1] == '': self.btn2['text'] = comp_turn

            elif (value[3] == value[4] != '') and value[5] == '': self.btn6['text'] = comp_turn
            elif (value[4] == value[5] != '') and value[3] == '': self.btn4['text'] = comp_turn
            elif (value[3] == value[5] != '') and value[4] == '': self.btn5['text'] = comp_turn

            elif (value[5] == value[7] != '') and value[8] == '': self.btn9['text'] = comp_turn
            elif (value[7] == value[8] != '') and value[6] == '': self.btn7['text'] = comp_turn
            elif (value[5] == value[8] != '') and value[7] == '': self.btn8['text'] = comp_turn

            elif (value[0] == value[3] != '') and value[6] == '': self.btn7['text'] = comp_turn
            elif (value[3] == value[6] != '') and value[0] == '': self.btn1['text'] = comp_turn
            elif (value[0] == value[6] != '') and value[3] == '': self.btn4['text'] = comp_turn

            elif (value[1] == value[4] != '') and value[7] == '': self.btn8['text'] = comp_turn
            elif (value[4] == value[7] != '') and value[1] == '': self.btn2['text'] = comp_turn
            elif (value[1] == value[7] != '') and value[4] == '': self.btn5['text'] = comp_turn

            elif (value[2] == value[5] != '') and value[8] == '': self.btn9['text'] = comp_turn
            elif (value[5] == value[8] != '') and value[2] == '': self.btn3['text'] = comp_turn
            elif (value[2] == value[8] != '') and value[5] == '': self.btn6['text'] = comp_turn

            elif (value[0] == value[4] != '') and value[8] == '': self.btn9['text'] = comp_turn
            elif (value[4] == value[8] != '') and value[0] == '': self.btn1['text'] = comp_turn
            elif (value[0] == value[8] != '') and value[4] == '': self.btn5['text'] = comp_turn

            elif (value[2] == value[4] != '') and value[6] == '': self.btn7['text'] = comp_turn
            elif (value[4] == value[6] != '') and value[2] == '': self.btn3['text'] = comp_turn
            elif (value[2] == value[6] != '') and value[4] == '': self.btn5['text'] = comp_turn

            else:
                try:
                    index =  value.index('X')
                except ValueError:
                    index = value.index('O')

                if index == 0:
                    select = random.choice([2, 4, 3])
                    if select == 2 and value[2] == '':
                        self.btn3['text'] = comp_turn
                    elif select == 4 and value[4] == '':
                        self.btn5['text'] = comp_turn
                    elif select==3 and value[3]=='':
                        self.btn4['text'] = comp_turn
                elif index == 1:
                    select = random.choice([6, 4, 8])
                    if select == 6 and value[6]=='':
                        self.btn7['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==8 and value[8]=='':
                        self.btn9['text'] = comp_turn
                elif index == 2:
                    select = random.choice([8, 4, 6])
                    if select == 8 and value[8]=='':
                        self.btn8['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==6 and value[6]=='':
                        self.btn7['text'] = comp_turn
                elif index == 3:
                    select = random.choice([6, 4, 2])
                    if select == 6 and value[6]=='':
                        self.btn7['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==2 and value[2]=='':
                        self.btn3['text'] = comp_turn
                elif index == 4:
                    select = random.choice([3, 5, 7])
                    if select == 3 and value[3]=='':
                        self.btn4['text'] = comp_turn
                    elif select == 5 and value[5]=='':
                        self.btn6['text'] = comp_turn
                    elif select==7 and value[7]=='':
                        self.btn8['text'] = comp_turn
                elif index == 5:
                    select = random.choice([6, 4, 2])
                    if select == 6 and value[6]=='':
                        self.btn7['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==2 and value[2]=='':
                        self.btn3['text'] = comp_turn
                elif index == 6:
                    select = random.choice([0, 4, 8])
                    if select == 0 and value[0]=='':
                        self.btn1['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==8 and value[8]=='':
                        self.btn9['text'] = comp_turn
                elif index == 7:
                    select = random.choice([0, 2, 4])
                    if select == 0 and value[0]=='':
                        self.btn1['text'] = comp_turn
                    elif select == 2 and value[2]=='':
                        self.btn3['text'] = comp_turn
                    elif select==4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                elif index == 8:
                    select = random.choice([3, 4, 5])
                    if select == 3 and value[3]=='':
                        self.btn4['text'] = comp_turn
                    elif select == 4 and value[4]=='':
                        self.btn5['text'] = comp_turn
                    elif select==5 and value[5]=='':
                        self.btn6['text'] = comp_turn
                else:
                    for i,v in enumerate(value, 1):
                        if value[i]=='':
                            if i==1:
                                self.btn1['text'] = comp_turn
                            elif i==2:
                                self.btn2['text'] = comp_turn
                            elif i==3:
                                self.btn3['text'] = comp_turn
                            elif i==4:
                                self.btn4['text'] = comp_turn
                            elif i==5:
                                self.btn5['text'] = comp_turn
                            elif i==6:
                                self.btn5['text'] = comp_turn
                            elif i==7:
                                self.btn7['text'] = comp_turn
                            elif i==8:
                                self.btn8['text'] = comp_turn
                            elif i==9:
                                self.btn9['text']  = comp_turn




if __name__ == '__main__':
    app = App()
    app.mainloop()