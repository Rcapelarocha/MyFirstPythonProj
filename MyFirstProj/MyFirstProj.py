

#------------------------------------------------------------------------BASICS


#print("Hello World!")
#print("Hello", end =" ")
#print("World!")

#------------------------------------------------------------------------Variables

#name = "Rafael"
#age = 19
#height = 5.4
#isAlive = True

#print(name + " " + str(age) + " " + str(height) + " " + str(alive))

#------------------------------------------------------------------------String Methods

#name = "python"

#print(name)
#print(len(name))
#print(name.find("y"))
#print(name.capitalize())
#print(name.upper())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("p"))
#print(name.replace("p","z"))
#print(name*5)

#------------------------------------------------------------------------Type Casting

#x = 1
#y = 2.0
#z = "3"

#print(x)
#print(int(y))
#print(3*float(z))

#-----------------------------------------------------------------------User Input

#print("what is your name")
#name = input()
#print ("your name is: " + name)

#print("What is your age")
#age = int(input())
#print(age*2)

        #OR

#age = int(input("How old are you"))
#print(age)

#-----------------------------------------------------------------------Useful Number Functions

#import math

#pi = -3.14
#x = 1
#y = 2
#z = 3

#print(pi)
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(69))
#print(max(x,y,z))
#print(min(x,y,z))

#------------------------------------------------------------------------String Slicing

#name = "Rafael Capela"

#firstName = name[0:6]
#lastName = name[7:13]
#stepName = name[::2]
#reverseName = name[::-1]

#print(firstName +" "+lastName)
#print(stepName)
#print(reverseName)



#website1 = "www.Google.com"
#website2 = "www.Yahoo.com"

#slice = slice(4, -4)

#print(website1[slice])
#print(website2[slice])

#------------------------------------------------------------------------ If Statements

#print("how old are you?")
#age = int(input())
#print(str(age))

#if age >= 18:
#    print("you are an adult")
#if age == 100:
#    print("you are old")
#elif age <0:
#    print("You are not born")
#else:
#    print("you are a child")

#------------------------------------------------------------------------Logical Oporators

#temp = int(input("what is the temperature: "))

#if temp >= 0 and temp <= 30:
#    print("temperature is good")
#
#elif not(temp == 100):
#    print("temp is not 100")
#
#elif temp <0 or temp > 30:
#    print("Temperature is bad")

#------------------------------------------------------------------------While Loops (limited or unlimited)

#while 1==1:
#        print("Infinite Loop")


#------------------------------------------------------------------------For Loop (limited)

#for i in range(10, 31, 2):  #(Start, End, Count by)
#    print(i)

#for i in "Hello":
#    print(i)

#import time 
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)

#-----------------------------------------------------------------------Nested For Loops

#for row in range(5):
#    for col in range(10):
#        print(row, end = " ")
#    print()

#-----------------------------------------------------------------------Loop Control Statements

#BREAK: breaks out of loop

#while True:
#    inp = input()
#    if inp == "B":
#        break


#CONTINUE:skips iteration of loop

#for i in "647-982-4553":
#    if i == "-":
#        continue
#    print(i, end = "")


#PASS: placeholder

#for i in range(1,21):
#    if i == 13:
#        pass
#    else:
#        print(i)

#------------------------------------------------------------------------Lists

#food = ["pizza", "iceCream", "spaghetti"]

#print(food[1])

#food.append("Hamburger")
#food.remove("pizza")
#food.pop()
#food.insert(1, "cake")
#food.sort()
#food.clear()
#print(len(food))

#for x in food:
#    print(x)

#------------------------------------------------------------------------2D Lists

#drinks = ["coffee", "soda", "tea"]
#dinner = ["pizza", "hamburger", "hotdog"]
#dessert = ["cake", "icecream"]

#food = [drinks, dinner, dessert]

#if "soda" in drinks:
#    print("soda is here")

#print (food[0][2])

#------------------------------------------------------------------------Tuple: Like Lists but Ordered and unchangable

#student = ("Rafael", 21, "male")

#print(student.count("Rafael"))
#print(student.index("male"))

#------------------------------------------------------------------------Set: collection that is ordered, unindexed. NO DUPLICATE VALUES

#utensils = {"fork", "spoon", "knife"}
#dishes = {"bowl", "plate", "knife"}

#utensils.add("napkin")
#utenisils.remove("fork")
#utenisils.clear()
#utensils.update(dishes)

#dinnerTable = utensils.union(dishes)           UNION           AUB
#dinnerTable = utensils.intersection(dishes)    INTERSECTION    A∩b
#dinnerTable = utensils.difference(dishes)      DIFFERENCE      A-B 

#for x in dinnerTable:
#    print(x)        #does not print in the same order

#------------------------------------------------------------------------Dictionary: changable unordered collection of unique (key:value) pairs

#capitals = {"USA": "Washington", 
#            "Canada": "Ottawa",
#            "Russion": "Moscow"}

#capitals.update({"China": "Beijing"})
#capitals.update({"USA": "Las Vegas"})
#capitals.pop("Canada")
#capitals.clear()

#print(capitals.get("USA"))
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key,value in capitals.items():
#    print(key, value)

#-------------------------------------------------------------------------Function

#def hello(name):
#    print("Hello " + name)
#    print("Have a nice day")


#hello("bro")
#hello("bro")
    
#------------------------------------------------------------------------Return

#def multiply(num1, num2):
#    return num1*num2
    

#NUM = multiply(8,6)
#print(NUM)

#------------------------------------------------------------------------Keyword Arguments: order of parameters dont matter

#def hello(first, last):
#    print("hello " + first + " " + last)

#hello(last ="capela", first="Rafael")

#------------------------------------------------------------------------*args: when a function accepts a varying amount of arguments. Compacts arguments into a tuple

#def add(*args):
#    sum = 0
    
#    for i in args:
#        sum = sum + i

#    return sum

#print(add(1,2,3))

#-----------------------------------------------------------------------Kwargs parameter that will pack all arguments into a dictionary

#def hello(**names):
#    print("Hello", end=" ")
#    for key,value in names.items():
#        print(value, end = " ")

#hello(first = "Rafael", middle = "Capela",last = "Rocha")

#-----------------------------------------------------------------------Format Method

#animal = "cow"
#item = "moon"
#item2 = "sun"

#print("The {} jumped over the {}".format(animal, item))
#print("The {0} jumped over the {2}".format(animal, item, item2))
#print("The {animal} jumped over the {item}".format(animal = "pig", item = "star"))

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Rafael"

#print("Hello my name is {}. Nice to meet you".format(name))
#print("Hello my name is {:10}. Nice to meet you".format(name))
#print("Hello my name is {:<10}. Nice to meet you".format(name)) #left
#print("Hello my name is {:>10}. Nice to meet you".format(name)) #right
#print("Hello my name is {:^10}. Nice to meet you".format(name)) #middle

#number = 3000

#print("The number is {:.2f}".format(number))
#print("The number is {:b}".format(number))  #binary
#print("The number is {:o}".format(number))  #octal
#print("The number is {:X}".format(number))  #hex

#-------------------------------------------------------------------------Random

#import random

#x = random.randint(1,6)
#y = random.random()

#myList = ['rock', 'paper', 'scissors']
#z = random.choice(myList)

#cards = [1,2,3,4,5,6,7,8,9,"J","Q", "K", "A"]
#random.shuffle(cards)

#print(x)
#print(y)
#print(z)
#print(cards)

#------------------------------------------------------------------------Exceptions

#try:
#    numerator = int(input("Enter a number to divide: "))
#    donominator = int(input("Enter a number to divide by"))
#    result = numerator/donominator

#except ZeroDivisionError as e:
#    print("Cant divide by zero")
#    print(e)
#except ValueError as e:
#    print("Enter only Numbers")
#    print(e)
#except Exception as e:
#    print("Something went wrong :(")
#    print(e)
#else:
#    print(result)
#finally:
#    print("This will always excecute")

#-------------------------------------------------------------------------File Detection

#import os

#path = "C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\text"

#if os.path.exists(path):
#    print("It exists")
#    if os.path.isfile(path):
#        print("It is a file")
#    elif os.path.isdir(path):
#        print("That is a directory")

#else:
#    print("that does not exist")

#-------------------------------------------------------------------------File Reading

#try:
#    with open('C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\text.txt') as file:
#        print(file.read())
#except FileNotFoundError:
#    print("file was not found")

#-------------------------------------------------------------------------File Writing

#text = "Dis some new txt yo\n"


#with open('C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\text.txt', 'a') as file:   # r: read w:write, overwrites existing file a:append, adds to the file
#    file.write(text)

#-------------------------------------------------------------------------File Coping

#import shutil

#shutil.copyfile('text.txt', 'copy.txt') #(name of file being copyed, name of copy) 
                                        #to change file copy location put path before name

#--------------------------------------------------------------------------Move File

#import os

#source = 'C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\MyFirstProj\\test.txt'
#destination = 'C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\\\MyFirstProj\\dest2\\test.txt'

#try:
#    if os.path.exists(destination):
#        print("file already exists")
#    else:
#        os.replace(source,destination)
#        print(source + " was moved")

#except FileNotFoundError:
#    print(source + ' not found')

#-----------------------------------------------------------------------------Deleting Files

#import os
#import shutil

#path = 'C:\\Users\\rafae\\OneDrive\\Documents\\Code\\Python\\MyFirstProj\\MyFirstProj\\dest2'

#try:    

    #os.remove(path)        #to delete file
    #os.rmdir(path)         #to delete empty folder
    #shutil.rmtree(path)    #to delete non-empty folder (dangeous)

#except FileNotFoundError:
#    print("file was not found")
#except PermissionError:
#    print("You do not have permission to delete that")
#except OSError:
#    print("You cannot delete that using that function")
#else:
#    print("file was deleted")

#------------------------------------------------------------------------------Modules

#import messages

#messages.hello()
#print(messages.add(1,1))

#OR

#import messages as msg

#msg.hello()

#OR

#from messages import hello

#hello()

#-----------------------------------------------------------------------------Object Oriented Programming

#class Car:

#    wheels = 4  #Class Variable

#    def __init__(self, make, model, year, color):
#        self.make = make    #Instance Variable
#        self.model = model  #Instance Variable
#        self.year = year    #Instance Variable
#        self.color = color  #Instance Variable
        

#    def drive(self):
#        print("this "+ self.model + " is driving")

#car_1 = Car("Chevy", "Corvette", 2021, "red")

#car_1.wheels = 2 #Affects just the current object
#print(car_1.model)
#print(car_1.wheels)

#Car.wheels = 3  #Affects all objects

#car_1.drive()

#-----------------------------------------------------------------------------Inheritance

#class Animal:

#    alive = True

#    def eat(self):
#        print("this animal is sleeping")

#class Rabbit(Animal):
#    def run(self):
#        print("this rabbit is running")

#class Fish(Animal):
#    def swim(self):
#        print("This fish is swimming")

#rabbit = Rabbit()
#fish = Fish()

#print(rabbit.alive)
#fish.eat()

#rabbit.run()
#fish.swim()

#-------------------------------------------------------------------------------Multiple Inheritance

#class Prey:
#    def flee(self):
#        print("This animal flees")

#class Predator:
#    def hunt(self):
#        print("This animal hunts")


#class Fish(Prey, Predator):
#    pass

#fish = Fish()

#fish.flee()
#fish.hunt()

#-------------------------------------------------------------------------------Method Chaining

#class Car:

#    def turn_on(self):
#        print("turn on")
#        return self #must return self

#    def drive(self):
#        print("drive")
#        return self #must return self

#car = Car()

#car.turn_on().drive()

#-------------------------------------------------------------------------------Super Function

#class Rectangle:

#    def __init__(self, length, width):
#        self.width = width
#        self.length = length

#class Square(Rectangle):

#    def __init__(self, length, width):
#        super().__init__(length, width)


#class Cube(Rectangle):

#    def __init__(self, length, width, height):
#        super().__init__(length, width)
#        self.height = height

#-------------------------------------------------------------------------------Abstract Classes - Template (Cannot make an object)

#from abc import ABC, abstractmethod

#class Vehicle(ABC):

#    @abstractmethod     #method to override
#    def go(self):
#        pass


#class Car(Vehicle):

#    def go(self):
#        print("Go! Car")

#car = Car()
#car.go()

#veh = Vehicle()

#-------------------------------------------------------------------------------Objects as Parameters

#class Car:

#    color = None

#def changeColor(vehicle, color):

#    vehicle.color = color;

#car = Car()

#print(car.color)

#changeColor(car, "red")
#print(car.color)

#--------------------------------------------------------------------------------Duck Typing - used when the methods/attributes are more important than the object

#class Duck:

#    def talk(self):
#        print("The duck is quaking")

#    def walk(self):
#        print("The duck is waddling")

#class Chicken:

#    def talk(self):
#        print("The chicken is clukking")

#    def walk(self):
#        print("The chicken is walking")


#class Person:

#    def catchDuck(self, duck):
#        duck.talk()
#        duck.walk()


#person = Person()
#duck = Duck()
#chicken = Chicken()

#person.catchDuck(duck)
#person.catchDuck(chicken)  #still works since chicken has same methods used in catchDuck as a duck object

#------------------------------------------------------------------------------------Walrus Oporator := - used to assign and use at the same time in one expression

#print(happy := True)

#foods = list()
#while food := input("What food do you need?") != "quit":    #assigns input to food and checks condition in one line 
#    foods.append(food)

#-----------------------------------------------------------------------------------Assign Fuction to a variable

#def hello():
#    print("hello")

#hi = hello
#hello()
#hi()

#say = print
#say("Wow")

#-----------------------------------------------------------------------------------Higher Order Functions - a function that either accepts a function as an argument 
#                                                                                                                                   or returns a function

#FIRST PART

#def loud(text):
#    return text.upper()

#def quiet(text):
#    return text.lower()

#def hello(funct):          #accepts function as parameter
#    text = funct("hello")
#    print(text)

#hello(loud)

#SECOND PART

#def divisor(x):
#    def dividend(y):
#        return y/x
#    return dividend        #returns function

#divide = divisor(2)     #sets 2 --> x, returns dividend
#print(divide(10))       #runs dividend(10)

#------------------------------------------------------------------------------------ Windows

#from tkinter import *

#widgets: GUI elements: buttons, textboxes, labels, images
#windows: a container to hold or contain widgets

#window = Tk()
#window.geometry("420x420")                  #sets size of window
#window.title("Title")

#icon = PhotoImage(file = "image.png")       #windows image icon
#window.iconphoto(True, icon)

#window.config(background = "#5cfcff")       #background colour
 

#window.mainloop()                           #places window on screen

#------------------------------------------------------------------------------------- Button

#from tkinter import *

#def click():
#    print("Hello!")
#    
#window = Tk()
#button = Button(window, text = "Click Me")
#button.config(command = click)
                                                #changing button looks
#button.config(bg = "red")
#button.config(fg = "blue")
#button.config(activebackground = "green")
#button.config(activeforeground = "yellow")

#image = PhotoImage(file = "icon.png")
#button.config(image = image)
#button.config(compound="top")           #to have label and image

#button.pack()                           #places button on window
#window.mainloop()

#------------------------------------------------------------------------------------- Entry(Textbox)

#from tkinter import *

#def submit():
#    username = entry.get()
#    print("hello " + username)
#    entry.config(state = DISABLED)

#def delete():
#    entry.delete(0,END)
    
#def backspace():
#    entry.delete(len(entry.get())-1,END)

#window = Tk()

#entry = Entry(window, font = ("Arial", 50), bg = "black", fg = "green", show = "*")
#entry.insert(0,"Default Text")
#entry.pack(side = LEFT)


#submit_button = Button(window, text = "Submit", command = submit)
#submit_button.pack(side = RIGHT)

#delete_button = Button(window, text = "Delete", command = delete)
#delete_button.pack(side = LEFT)

#backspace_button = Button(window, text = "Backspace", command = backspace)
#backspace_button.pack(side = LEFT)

#window.mainloop()

#--------------------------------------------------------------------------------------- Label
#from tkinter import *

#window = Tk()

#photo = PhotoImage(file = 'icon.png')

#label = Label(window,  
#              text = "Hello World",
#              font = ("Arial", 40, "bold"),
#              fg = 'green', 
#              bg = 'red',
#              relief = RAISED,  #Boarder
#              bd = 10,
#              padx = 20,
#              pady = 20,
#              image = photo)

#label.place(x = 10, y = 0)

#window.mainloop()

#-------------------------------------------------------------------------------------- Check Boxes

#from tkinter import *

#def display():
#    if x.get() == 1:
#        print("True")
#    else:
#        print("false")
    

#window = Tk()
#x = IntVar()

#photo = PhotoImage(file = 'photo.png')

#checkButton = Checkbutton(window,
#                          text = 'I agree to something',
#                          variable = x,
#                          onvalue=1,    #can return different vals: string, bool, int
#                          offvalue=0,
#                          command = display,
#                          font = ('Arial', 20),
#                          fg = 'red',
#                          bg = 'black',
#                          activebackground= 'black',
#                          activeforeground= 'pink',
#                          padx = 20,
#                          pady = 20,
#                          image = photo)

#checkButton.pack()
#window.mainloop()

#------------------------------------------------------------------------------------------- Radio Buttons - similar to checkboxes but can only select one

#from tkinter import *

#foods = ["pizza", 'hamburger', 'hotdog']

#def order():
#    print(x.get())

#window = Tk()
#x = IntVar()

#for i in range(len(foods)):
    
#    radiobutton = Radiobutton(window,
#                              text=foods[i],    #text of radio buttons
#                              variable = x,     #groups radiobuttons if they share the same variable, only one button can be selected from the group
#                              value = i,        #assigns each button a different value
#                              command = order,
#                              indicatoron = 0,  #removes ciecle indicators
#                              width = 15)       #changes width of buttons
    
#    radiobutton.pack(anchor = 'w')          #w: west, 
    
#window.mainloop()

#------------------------------------------------------------------------------------------- Sliding Scale

#from tkinter import *

#window = Tk()

#def submit():
#    print('Number:' + str(scale.get()))

#scale = Scale(window,
#              from_ = 0,
#              to_ = 100,
#              length = 600,
#              orient = HORIZONTAL,
#              showvalue=1,      # 1: show number, 0: dont show number
#              tickinterval=10,  
#              #resolution=25,    #increment of slider, messes with ticks
#              troughcolor = 'red',
#              fg = 'blue',
#              bg = 'yellow')
#button = Button(window, text = 'submit', command = submit)

#button.pack()
#scale.pack()
#window.mainloop()

#----------------------------------------------------------------------------------------------- Frame

#from tkinter import *

#window = Tk()

#frame = Frame(window)
#frame.pack()

#button1 = Button(frame, text='w').pack(side = TOP)
#button2 = Button(frame, text = 'a').pack(side = LEFT)
#button3 = Button(frame, text = 's').pack(side = LEFT)
#button4 = Button(frame, text = 'd').pack(side = LEFT)

#window.mainloop()

#---------------------------------------------------------------------------------------------- Grid

#from tkinter import *

#window = Tk()

#titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

#firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
#firstNameEntry = Entry(window).grid(row=1,column=1)

#lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
#lastNameEntry = Entry(window).grid(row=2,column=1)

#emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
#emailEntry = Entry(window).grid(row=3,column=1)

#submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

#window.mainloop()

#----------------------------------------------------------------------------------------------- Progress Bar

#from tkinter import *
#from tkinter.ttk import *
#import time

#def start():
#    tasks = 10
#    x = 0
#    while(x<tasks):
#        time.sleep(1)
#        bar['value'] += 10
#        x+=1
        
#        window.update_idletasks()

#window = Tk()

#bar = Progressbar(window, orient=HORIZONTAL, length = 300)
#bar.pack()

#button = Button(window, text = 'submit', command = start).pack()

#window.mainloop()

#----------------------------------------------------------------------------------------------- Canvas
#from tkinter import *
#from tkinter.ttk import Style

#window = Tk()

#canvas = Canvas(window, height = 500, width = 500)
#blueLine = canvas.create_line(0,0,500,500, fill = 'blue', width = 5)
#rectangle = canvas.create_rectangle(50,50,250,250, fill = 'blue')
#triangle = canvas.create_polygon(250,0, 500,500, 0,500,fill = 'cyan', outline = 'black', width = 5)
#arc = canvas.create_arc(0,0,500,500, fill = 'green', style = PIESLICE, start = 180, extent = 180)
#circle = canvas.create_oval(190,190,310,310, fill = 'black')
#canvas.pack()

#window.mainloop()

#------------------------------------------------------------------------------------------------ Scrolling

#from tkinter import *

#window = Tk()
#window.geometry('600x400')

#canvas = Canvas(window, bg = 'black', scrollregion = (0,0,2000,5000))
#canvas.pack(expand = True, fill = 'both')
#canvas.create_line(0,0,2000,5000, fill = 'white')

#Scrolling Bar

#scrollbar = Scrollbar(window, orient = 'vertical', command = canvas.yview)
#canvas.configure(yscrollcommand = scrollbar.set)
#scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')


#Mouse Scrolling
#canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta/60), "units"))

#window.mainloop()

#-----------------------------------------------------------------------------------------------