#This project Snake and ladder is developed using python
#with an aim to recreate the classical board game snakes
#and ladders which is an ancient Indian board game that's
#regarded today as a worldwide classic.
#T IS MADE WITH THE HELP OF FOLLOWING PYTHON MODULES:
#1. Tkinter,2. PIL,3. Random,4. OS

import tkinter as tk
from PIL import Image, ImageTk
import random
import os



    

def start_game():
    global im
    global b1,b2


    #BUTTON 1
    b1.place(x=775,y=100)
    #BUTTON-2
    b2.place(x=775,y=250)

    #BUTTON(EXIT)

    b4=tk.Button(root,text="EXIT",height=2,width=15,fg='black',bg='red',font=('cursive',10,'bold'),activebackground='yellow',command=root.destroy)
    b4.place(x=830,y=650)


    #DICE
    im=Image.open("dice.png")
    im=im.resize((65,65))
    im=ImageTk.PhotoImage(im)
    b3=tk.Button(root,image=im,height=80,width=80,bg="purple")
    b3.place(x=850,y=450)


def reset_coins():
    global p1,p2
    global pos1,pos2

    p1.place(x=0,y=720)
    p2.place(x=50,y=720)

    pos1=0
    pos2=0

def load_diceimg():
    global dice
    names=["1.png","2.png","3.png","4.png","5.png","6.png"]
    for nam in names:
        im=Image.open("C:\\img\\"+nam)
        im=im.resize((65,65))
        im=ImageTk.PhotoImage(im)
        dice.append(im)


def check_ladder(Turn):
    global pos1,pos2
    global ladder

    f=0 #no ladder
    if Turn==1:
        if pos1 in ladder:
            pos1=ladder[pos1]
            f=1
    else:
        if pos2 in ladder:
            pos2=ladder[pos2]
            f=1
    return f
            
def check_snake(Turn):
    global pos1,pos2

    if Turn==1:
        if pos1 in snake:
            pos1=snake[pos1]

    else:
        if pos2 in snake:
            pos2=snake[pos2]
                
            
def roll_dices():
    global dice
    global turn
    global pos1,pos2
    global b1,b2
    
    r=random.randint(1,6)
    b=tk.Button(root,image=dice[r-1],height=80,width=80)
    b.place(x=850,y=450)

   # speak(str(r))


    lad=0
    if turn==1:
       if (pos1+r)<=100:
           pos1=pos1+r
       lad=check_ladder(turn)
       check_snake(turn)
       move_coin(turn,pos1)
       if r!=6 and r!=1 and r!=5:
           turn=2
           b1.configure(state='disabled')
           b2.configure(state='normal')
    else:
        if (pos2+r)<=100:    
            pos2=pos2+r
        lad=check_ladder(turn)
        check_snake(turn)
        move_coin(turn,pos2)
        if r!=6 and r!=1 and r!=5:
            turn=1
            b1.configure(state='normal')
            b2.configure(state='disabled')


        is_winner()
     
def is_winner():
    global pos1,pos2

    if pos1==100:
        msg=' PLAYER-1 IS THE WINNER!!!'
        Lab=tk.Label(root,text=msg,height=2,width=25,bg='red',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
        msg=' PLAYER-2 IS THE WINNER!!!'
        Lab=tk.Label(root,text=msg,height=2,width=25,bg='blue',font=('cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()


    
def move_coin(Turn,r):
    global p1,p2
    global index

    if Turn==1:
        p1.place(x=index[r][0],y=index[r][1])
    else:
        p2.place(x=index[r][0],y=index[r][1])
        


def get_index():
    global p1,p2
    num=[100,99,98,97,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    row=20
    i=0
    for x in range(1,11):
        col=20
        for y in range(1,11):
            index[num[i]]=(col,row)
            col=col+70
            i=i+1
        row=row+70
    
    
        
#store dice img
dice=[]
#store x and y

index={}

#int pos
pos1=None
pos2=None

#ladder
ladder={2:45,9:50,14:76,21:59,48:86,72:91,80:99}

#snake
snake={98:77,93:68,85:17,69:28,62:36,34:4,22:4}

root = tk.Tk()
root.geometry("1100x800")
root.title("SNAKE AND LADDER")

f1=tk.Frame(root,width=1000,height=800,relief='raised')
f1.place(x=0,y=0)


#BOARD
img1= ImageTk.PhotoImage(Image.open("C:\\img\\slboard.png"))
lab=tk.Label(f1,image=img1)
lab.place(x=0,y=0)

#p1 button
b1=tk.Button(root,text="PLAYER-1",height=3,width=20,fg='blue',bg='cyan',font=('cursive',14,'bold'),activebackground='yellow',command=roll_dices)
#p2 button
b2=tk.Button(root,text="PLAYER-2",height=3,width=20,fg='red',bg='cyan',font=('cursive',14,'bold'),activebackground='yellow',command=roll_dices)


#coin 1
p1=tk.Canvas(root,width=40,height=40)
p1.create_oval(10,10,40,40,fill='blue')
 

#coin 2
p2=tk.Canvas(root,width=40,height=40)
p2.create_oval(10,10,40,40,fill='red')
 
turn=1



reset_coins()
get_index()
load_diceimg()
start_game()


root.mainloop()
