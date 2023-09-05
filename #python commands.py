#python commands

#math
#print(round(pi))
# nearest whole integer

#print(math.ceil(pi))

#print(math.floor(pi))

#print(abs(pi))

#print(pow(pi, 2))
#pi to the power of two

#print(math.sqrt(420))

#print(max(x, y, z))
#print(min(x, y, z))


#slicing
#[start:stop:step]


#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

#tuple 
#student = ("Johnny",21,"Lin")
#print(student.count("bro"))
#for x in student
#print(x)
# tuple = ordered and unchangeable unlike lists
# set = collection which is unordered, unindexed. No duplicate values
#dictionary: changable, unordered key value pair
#*args = pack all arguments into a single tuple
#**kwargs =  pack all arguments into a dictionary
def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
hello(first = "Johnny", middle = "dude", last="ok")

# str.format
# 1000
# {:3f} adds .000
# {:,} adds , separator
# {:b} changes to binary
# {:o} octa
# {:X} 3E8
# {:E} scientific number

#import random
#random.choice(myList)
#random.shuffle(cards)
#print(cards)

#exception handling
try:
    sdsd
except ZeroDivisionError as e:
    print(e)
    print("Enter...")

import os
path = "C:\\Users\\JL\\Desktop\\test.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("this is a directory")
try:
    with open('C:\\Users\\JL\\Desktop\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

text = "fhfjd"

with open('C:\\Users\\JL\\Desktop\\test.txt', 'w') as file:
    file.write(text)
    #will overwrite

#copyfile() = copies contents of a file
#copy() =  copyfile() + permission mode + destination can be a directory
# copy2() =  copy() + copies metadata (file's creation and modification times)
import shutil
shutil.copyfile('test.txt', 'copy.txt')

source = "test.txt"
destination = "C:\\Users\\Desktop"
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
