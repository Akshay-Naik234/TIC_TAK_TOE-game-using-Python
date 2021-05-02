from tkinter import *
from tkinter import messagebox

def disable_all():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state = 'disable')

def callback(r,c):
    global count
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X',fg='blue',bg='white')
        states[r][c] = 'X'
        player = 'O'
        count+=1

    elif player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O',fg='orange',bg='black')
        states[r][c] = 'O'
        player = 'X'
        count+=1

    elif states[r][c] != 0:
        messagebox.showerror('TIC TAC TOE','ALREADY FILLED')
    

    check_for_winner()
    
def check_for_winner():
    global stop_game,count
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            b[i][0].config(bg = 'grey')
            b[i][1].config(bg = 'grey')
            b[i][2].config(bg = 'grey')
            stop_game = True
            if states[i][0] + states[i][1] +states[i][2] == 'XXX':
                messagebox.showinfo('TIC TAC TOE','X WINS')
            else:
                messagebox.showinfo('TIC TAC TOE','O WINS')

            disable_all()
            
    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] !=0:
            b[0][i].config(bg = 'grey')
            b[1][i].config(bg = 'grey')
            b[2][i].config(bg = 'grey')
            stop_game = True
            if states[0][i] + states[1][i] + states[2][i] == 'XXX':
                messagebox.showinfo('TIC TAC TOE','X WINS')
            else:
                messagebox.showinfo('TIC TAC TOE','O WINS')
            disable_all()
            
    if states[0][0] == states[1][1] == states[2][2] !=0:
        b[0][0].config(bg = 'grey')
        b[1][1].config(bg = 'grey')
        b[2][2].config(bg = 'grey')
        stop_game = True
        if states[0][0] + states[1][1] + states[2][2] == 'XXX':
            messagebox.showinfo('TIC TAC TOE','X WINS')
        else:
            messagebox.showinfo('TIC TAC TOE','O WINS')
        disable_all()
            
    elif states[2][0] == states[1][1] == states[0][2] !=0:
        b[2][0].config(bg = 'grey')
        b[1][1].config(bg = 'grey')
        b[0][2].config(bg = 'grey')
        stop_game = True
        if states[2][0] + states[1][1] + states[0][2] == 'XXX':
            messagebox.showinfo('TIC TAC TOE','X WINS')
        else:
            messagebox.showinfo('TIC TAC TOE','O WINS')
        disable_all()

    elif count == 9 and stop_game == False:
        messagebox.showinfo('TIC TAC TOE','IT IS TIE')
        stop_game = True
        disable_all()
                
root = Tk()
root.title('TIC TAC TOE')

def reset():
    global b,states,player,stop_game,count
    count = 0
    b = [[0,0,0],
         [0,0,0],
         [0,0,0]]
    states = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    player = 'X'
    stop_game = False
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(font = ("Arial",60),width = 4 ,bg='powder blue',command=lambda r=i,c= j:callback(r,c))
            b[i][j].grid(row=i,column=j)

reset_b= Button(root, text = 'RESET',font=('TIMES NEW ROMAN',20),height = 1,width=6,bg = 'silver',command=reset)
reset_b.grid(row = 3,column =1)
reset()

