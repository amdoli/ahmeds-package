def checkint(value):
    condetion="None"
    numb=[]
    for i in range(10):
        numb.append(str(i))
    listvalue=list(str(value))
    for i in range(len(listvalue)):
        for j in range(10):
            if numb[j]==listvalue[i]:
                break
            elif j==9 and numb[j]!=listvalue[i]:
                condetion="False"
                break                
    if condetion=="False":
        return "False"
    else:
        return "True"

def writeint():
    what=input("write something and I will check if it's integer or not: ")
    result=checkint(what)
    if result=="False":
        print("It has a str\n")
    else:
        print("It's an integer!\n")
