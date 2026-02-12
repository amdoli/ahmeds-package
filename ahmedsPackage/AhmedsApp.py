from ahmedsPackage import *
import time

def ahmedsApp():
    print("now you kinda made an app that have sevreal tasks")
    while True:
        while True:
            time.sleep(1)
            which=input("choose a task [check int, calc,(read & write a file), OS]\n")
            time.sleep(0.5)
            if which.lower() in ["check int", "int","check"]:
                writeint()
                break
            elif which.lower() in ["calc", "calculator","calculate"]:
                calc()
                break
            elif which.lower() in ["read","r","write","file","read & write a file","(read & write a fiie)"]:
                AhmedsRead_Write()
                break
            elif which.lower() in ["os","oberating system","system"]:
                ahmedsOs()
                break
            elif which.lower() in ["name","whats your name"]:
                whatsyourname()
                break
            else:
                print("sorry I didn't understand you")
                time.sleep(1)
                print("please write again!\n")
                time.sleep(0.5)
        wish=input("do you wish to contenue? [Yes,No]\n")
        if wish.lower() in ["no","n","stop"]:
            break
        elif wish.lower() in ["yes","yeah","y"]:
            continue
    time.sleep(1)
    print("\nhave a good day")
