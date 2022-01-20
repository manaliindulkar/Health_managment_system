import datetime
def gatetime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("1.for exercise or 2 for food"))
        if c==1:
            value=input("type here:\n")
            with open("harry_r","a")as op:
                op.write(str([str(gatetime())])+" "+value+"\n")
                print("successfully written")
        elif c==2:
            value=input("type here:\n")
            with open("harry_l","a")as op:
                op.write(str([str(gatetime())])+" "+value+"\n")
                print("successfully written")
    elif k==2:
        c=int(input("1.for exercise or 2 for food"))
        if c==1:
            value = input("type here:\n")
            with open("rohan_r", "a")as op:
                op.write(str([str(gatetime())]) + " " + value + "\n")
                print("successfully written")
        elif c==2:
            value = input("type here:\n")
            with open("rohan_l", "a")as op:
                op.write(str([str(gatetime())]) + " " + value + "\n")
                print("successfully written")
    elif k==3:
        c=int(input("1. for exercise or 2.for food"))
        if c==1:
            value = input("type here:\n")
            with open("haman_r", "a")as op:
                op.write(str([str(gatetime())]) + " " + value + "\n")
                print("successfully written")
        elif c==2:
            value=input("type here:\n")
            with open("haman_l","a")as op:
                op.write(str[str(gatetime())]+" "+value+"\n")
                print("successfully written")
    else:
        print("please enter valid input namme")

def retrive(k):
    if k==1:
        c=int(input("enter 1 for excercise or 2 for food"))
        if c==1:
            with open("harry_r")as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("harry_l")as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c=int(input("enter1 .for excercise or 2. for food"))
        if c==1:
            with open("rohan_r")as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("rohan_l")as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c=int(input("enter 1 foe excercise or 2. for food"))
        if c==1:
            with open("haman_r")as op:
                for i in op:
                    print(i, end="")
        elif c==2:
            with open("haman_l")as op:
                for i in op:
                    print(i, end="")
    else:
        print("enter valid name")
print("Health Management System")
a=int(input("press 1 for lock and 2 for retrive\n"))
if a==1:
    b=int(input("1.Harry\n 2.rohan\n3.Haman"))
    take(b)
else:
    b=int(input("1.Harry\n 2.rohan\n3.Haman"))
    retrive(b)





