

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

#-------------------------------------------------------------------------------Abstract Classes



