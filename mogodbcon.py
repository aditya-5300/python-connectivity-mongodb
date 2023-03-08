from tkinter import *
import pymongo
from pymongo import collection
root=Tk()
root.minsize(500,500)
root.maxsize(500,500)
root.title("My first Gui")
root.config(bg="White")
namev=StringVar()
roll_nov=StringVar()
def sub():
    client=pymongo.MongoClient("mongodb://localhost:27017")
    db=client['gui']
    collection=db["aditya"]
    dic={
        'name':namev.get(),
        'roll_no':roll_nov.get()
    }
    collection.insert_one(dic);
def sub2():
    client=pymongo.MongoClient("mongodb://localhost:27017")
    db=client['gui']
    collection=db["aditya"]
    dic={
        'name':namev.get(),
        'roll_no':roll_nov.get()
    }
    collection.delete_one(dic)
def sub3():
    client=pymongo.MongoClient("mongodb://localhost:27017")
    db=client['gui']
    collection=db["aditya"]
    myquery = { "name": namev.get() }
    newvalues = { "$set": { "name":"updated name" } }
    collection.update_one(myquery,newvalues)

head=Label(text="My first Gui")
head.place(x=10,y=25)
name=Label(text="Name")
name.place(x=20,y=50)
e=Entry(text=namev)
e.place(x=20,y=75)
roll=Label(text="Roll_No")
roll.place(x=20,y=125)
roll_e=Entry(text=roll_nov)
roll_e.place(x=20,y=150)
b=Button(text="Insert",command=sub)
b.place(x=150,y=200)
b2=Button(text="Delete",command=sub2)
b2.place(x=100,y=200)
b3=Button(text="update",command=sub3)
b3.place(x=250,y=200)
root.mainloop()
