import os
import time
from .AhmedsRead_Writef import AhmedsRead_Write


# there is small in line 28 problem but it works
# bruhhhhh that was my old code past 1 week I was so ass
# and yes I will keep it to watch how I was before!

#def showfiles():
#    os.chdir("/")
#    x=True
#    print("\nwrite the file you want to navigate\n")
#    while x==True:
#        files=os.listdir()
#        print(files)
#        wanted=input("")
#        while True:
#            y=True
#            if wanted.lower in ["stop","s"]:
#                break
#            else:
#                for i in range (len(files)):
#                    if wanted==files[i]:
#                        os.chdir(wanted)
#                        time.sleep(0.5)
#                        print("\n")
#                        break
#                    elif (i==(len(files)-1)) and y==True and (wanted.lower() != "stop","s"):
#                        time.sleep(0.5)
#                        print("please try again!\n")
#                        time.sleep(0.5)
#            break
#        if wanted.lower() in ["stop","s"]:
#            break


# to navigate
def showfiles():
    print("\nwrite the file you want to navigate\n")
    while True:
        files=os.listdir()
        print(f"{files}\n")
        wanted=input("")
        if wanted in files:
            for file in files:
                if wanted==file:
                    try:
                        os.chdir(file)
                    except NotADirectoryError:
                        time.sleep(0.5)
                        print("That's not a directory!")
                        time.sleep(0.5)
        elif wanted =="~/":
            os.chdir("home")
            users=os.listdir()
            for user in users:
                if user!="liveuser":
                    os.chdir(user)   
        elif wanted.lower() in ["stop","exit","s","alt+f4"]:
            print("\n")
            time.sleep(0.5)
            break
        else:
            print("invalid!")
            print("please try again!\n")



# to make a file
def makefile():
    mhan={"slados","saldos","salados","satos","sados","sashos","seldos","sedos","sandos","sasoos"}
    dirname=input("what do you want to name it?\n")
    time.sleep(0.5)
    if dirname in mhan:
        confused="..."
        for dot in confused:
            print(dot)
            time.sleep(0.5)
        print("you know what you are writing right?")
        time.sleep(2)
    os.mkdir(dirname)
    print(f"the {dirname} directory created succesfully!")
    time.sleep(1)

# to remove a file 
# I was about to commit a sucide when I was writing this function
# actually after I returned to the code it wasn't that hard but I was stupid and beginner before!
def remove():
    x=0
    mhan={"slados","saldos","salados","satos","sados","sashos","seldos","sedos","sandos","sasoos"}
    while x<4:
        items=os.listdir()
        print(items)
        deldir=input("\nwhat do you want to delete?              (if you want to stop just write [stop]\n")
        time.sleep(0.5)
        if deldir.lower() in ["slados","saldos","salados","satos","sados","sashos","seldos","sedos"]:
            if mhan.intersection(items):
                os.rmdir(deldir)
                time.sleep(1)
                print("yessssss tm ahana saladooooooooooos\n")
                time.sleep(1)
                break
            else:
                print("lets dele")
                time.sleep(1)
                print("wait")
                time.sleep(0.5)
                print("fuck I wish salados was exsisted so I can delete it and ahenh")
                x=0
                time.sleep(2)
        elif deldir.lower() in ("I changed my mind","I don't want to","stop","no","I don't want to delete","I don't want to delete anymore"):
            time.sleep(0.3)
            print("as you wish sir!")
            time.sleep(1)
            break
        # here are the real remove 
        else:
            if deldir in items:
                for file in items:
                    if deldir == file:
                        time.sleep(0.5)
                        sure=input(f"you are about to delete {file} are sure? [yes/no]\n")
                        time.sleep(0.5)
                        if sure in ["yes","y","yup"]:
                            try:
                                os.rmdir(file)
                                time.sleep(0.5)
                                print("the file has deleted succesfully!")
                                x=4
                            except NotADirectoryError:
                                print("that is not a directory!\n")
                                time.sleep(0.5)
                                print("you can't delete it!\n")
                                time.sleep(0.5)
                        if sure.lower() in ["no","n"]:
                            print("ok!")
                            x=4
            else:
                if x<3:
                    print("I didn't find what you asked")
                    time.sleep(1)
                    print("please try again:\n")
                    x+=1
                else:
                    time.sleep(0.5)
                    print("you are trolling!")
                    time.sleep(1)
                    print("get out!!!!!")
                    time.sleep(1)
                    exit()


# --------------------------------------------------------------------------------------------MAIN FUNC--------------------------------------------------------------------------------------------
def oberations():
    while True:
        x=0
        items=os.listdir()
        print("hello")
        time.sleep(1)
        chose=input("choose one of the operations [list directory,make directory, remove directory, change a directory, read & write a file]\n")
        time.sleep(0.5)
        #li
        if chose.lower() in ["list files","li","l","listdir","list"]:
            print(items)
        #mk
        elif chose.lower() in ["mk","make","mkdir","make directory","m"]:
            makefile()
        #rm
        elif chose.lower() in ["rm","r","remove","remove directory","rmdir"]:
            remove()  
        elif chose.lower() in ["stop","s","alt+f4","exit","end"]:
            print("\n")
            break 
        elif chose.lower() in ["read","r","write","file","read & write a file","(read & write a fiie)"]:
            AhmedsRead_Write()
        elif chose.lower() in ["change","chdir","ch","change a","change a directory","c"]:
            showfiles()
        else:
            print("\nsorry I didn't understand you")
            time.sleep(1)
            print("please try again!")
            time.sleep(1)
        print("\n")

# asking for a name
# it's not related to the main func but I keep it here becuase it's kinda related to OS
def whatsyourname():
    username=os.environ.get("USER")
    name=input("whats your name?")
    time.sleep(0.5)
    print(f"so your name is {name} ")
    time.sleep(1)
    print(f"are you sure it's not {username}?")
    time.sleep(2)
    print("naah Im just kidding I just said a random name imagin I said your name by accident how funny hahahahahaha")

# determine which operating system the user uses
# that will be cooked later to make the code cross-platform because now it's linux based (maybe it works in windows but with bugs)
 
def choosing():
    system=os.name
    if system=="posix":
        pass
    elif system=="nt":
        pass

# still cooking this one not finished yet
# it's kinda finished but without Desktop and Downloads options because I didn't put the windows option!
def ahmedsOs():
    while True:
        print("where you want to make the chemecals?")
        where=input("[Desktop,Downloads,elsewhere]\n")
        time.sleep(0.5)
        if where.lower()=="elsewhere":
            print("to make it easier I will start from the beginning you will chose the where till you say (stop)")
            time.sleep(2)
            os.chdir("/")
            showfiles()
            oberations()
            break
        elif where.lower() in ["desktop","downloads"]:
            print("to be honest I didn't write a code for a windows until now it's only works on linux")
            time.sleep(4)
            print("and I don't have the time to write it now")
            time.sleep(2)
            print("utleast right now")
            time.sleep(1)
        elif where.lower in ["stop","exit","s","no","n","alt+f4"]:
            print("as you wish!")
            break
        else:
            print("please try again!\n")
            time.sleep(0.5)

