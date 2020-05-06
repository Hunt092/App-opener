# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:17:00 2020

@author: Yash Chavan
"""


import tkinter as tk
from tkinter import  filedialog
import os
height=600
width=800
button_font=('Berlin Sans FB Demi',20,'bold')
text_font=('Comic Sans MS',12)
Apps=[]
root=tk.Tk()

if os.path.isfile("savefile.txt"):
    with open('savefile.txt','r') as scr:
        temp =scr.read()
        temp = temp.split(',')
        Apps = [a for a in temp if a.strip()]
        
        
def Get_app():
    
    for widget in frame.winfo_children():
        widget.destroy()
            

    filename= filedialog.askopenfilename(initialdir="/",title="Select File",
                                         filetypes=(('executible','*.exe'),('all file','*.*')))
    
    Apps.append(filename)
    for app in Apps:
        Appname = tk.Label(frame,text=app,bg='#d9d9d9',font=text_font,wraplength=650,bd=5)
        Appname.pack()
        
def Runapp():
    for app in Apps:
        os.startfile(app)
        
def Delete_app():
    for widget in frame.winfo_children():
        widget.destroy()
    Apps.clear()
    if os.path.exists("savefile.txt"):
        os.remove("savefile.txt")
    else:
        print("The file does not exist")
    
canvas = tk.Canvas(root,heigh=height,width=width,bg='#999999',relief='sunken',bd=3)
canvas.pack()

frame= tk.Frame(canvas,bg='#b3b3b3',relief='raised',bd=1,pady=12)
frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

App= tk.Button(root,text="Get app",padx=5,pady=5,command=lambda:Get_app(),
               font=button_font,relief='flat',activebackground='#595959',
               activeforeground='#e6e6e6')
App.pack(side='left')

Run= tk.Button(root,text="Run apps",padx=5,pady=5,command=lambda:Runapp(),
               font=button_font,relief='flat',activebackground='#595959',
               activeforeground='#e6e6e6')
Run.pack(side='right')

Delete = tk.Button(root,text="Delete apps",padx=5,pady=5,command=lambda:Delete_app(),
                   font=button_font,relief='flat',activebackground='#595959',
                   activeforeground='#e6e6e6')
Delete.pack()

for app in Apps:
       Appname = tk.Label(frame,text=app,bg='#d9d9d9',font=text_font,wraplength=650,bd=5)
       Appname.pack()

root.mainloop()

with open('savefile.txt','w') as scr:
    for app in Apps:
        scr.write(app +',')
