# let us begin with building a simple quiz

print("welcome to the hunger games quiz!")
username = input("Enter your game name") # user will enter the username used throughout the game in the variable username
print("You will be" + username)
from tkinter import *        


from tkinter.ttk import *

root = Tk() 
  
root.geometry('100x100')     

btn = Button(root, text = 'Click me !', 
                command = root.destroy) 

btn.pack(side = 'top')     

root.mainloop() 
