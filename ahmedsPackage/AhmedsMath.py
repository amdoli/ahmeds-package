import time
from .AhmedsCheckInt import checkint

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        pass
    else:
        return x/y

def user2numb():
    while True:
        while True:
            x=input("enter the first number: ")
            if checkint(x)=="False":
                print("you wrote a str!")
                time.sleep(0.5)
                print("please write only an intgers!")
            else:
                break
        while True:
            time.sleep(0.5)
            y=input("enter the second number: ")
            if checkint(y)=="False":
                print("you wrote a str!")
                time.sleep(0.5)
                print("please write only an intgers!")
            else:
                break
            break
        return int(x),int(y)


def calc():
    while True:
        print("hello and welcome to our calculator!\n")
        time.sleep(1)
        which=input("what operation do you want?[+,-,*,/]\n")
        if (which=="+") or (which.lower()=="sum") or (which.lower()=="plus"):
            x,y=user2numb()
            result=add(x,y)
            break
        elif which.lower() in ["-","minus","subtract"]:
            x,y=user2numb()
            result=subtract(x,y) 
            break 
        elif which.lower() in ["*","mult","multybly"]:
            x,y=user2numb()
            result=mult(x,y) 
            break
        elif which.lower() in ["/","divide","over"]:
            x,y=user2numb()
            result=div(x,y)
            if result == None:
                result="ininty"
            break
        else:
            print("ether you wrote it wrong Or I didn't understand you")
            time.sleep(1)
            print("please write again!\n")
            time.sleep(0.5)
    time.sleep(0.5)
    print(f"\nthe result are {result}")
        
