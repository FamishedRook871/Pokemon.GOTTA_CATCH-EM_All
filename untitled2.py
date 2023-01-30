from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("Pokemon Battles")
root.geometry("800x600")
root.configure(background="orange")
img=ImageTk.PhotoImage(Image.open("button.jpg"))
ArceusV = ImageTk.PhotoImage(Image.open("ArceusV.jpg"))
CharizardV = ImageTk.PhotoImage(Image.open("CharizardV.jpg")) 
HoundoomEX = ImageTk.PhotoImage(Image.open("HoundoomEX.jpg"))
LugiaV = ImageTk.PhotoImage(Image.open("LugiaV.jpg"))
MewtwoV = ImageTk.PhotoImage(Image.open("MewtwoV.jpg"))
ZamazentaV = ImageTk.PhotoImage(Image.open("ZamazentaV.jpg"))
Zekrom = ImageTk.PhotoImage(Image.open("Zekrom.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)
player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor = CENTER)
player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor = CENTER)
player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor = CENTER)


Pokemonlist = [ArceusV, CharizardV, HoundoomEX, LugiaV, MewtwoV, ZamazentaV, Zekrom]
Powerlist = [220, 220, 170, 220, 220, 220, 130]
label = Label(root)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
player1score=0
def player1():
    global player1score
    random_no=random.randint(0,6)
    random_pokemon=Pokemonlist[random_no]
    label["image"]=random_pokemon
    random_power_list = Powerlist[random_no]
    player1_score = player1score + random_power_list
    player_1_score_label["text"] = str( player1_score)
    
player2score=0
def player2():
    global player2score
    random_no=random.randint(0,6)
    random_pokemon=Pokemonlist[random_no]
    label["image"]=random_pokemon
    random_power_list = Powerlist[random_no]
    player2_score = player2score + random_power_list
    player_2_score_label["text"] = str( player2_score)
    

player_1_btn = Button(root, height=30, width=30, image = img, command = player1)    
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor = CENTER)
player_2_btn = Button(root, height=30, width=30, image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor = CENTER)
root.mainloop()