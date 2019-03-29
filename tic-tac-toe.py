import random
bord = ["-" , "-" , "-",
       "-"  , "-" , "-",
       "-" ,"-" ,  "-"]
def display_bord():
    print (bord[0],"|",bord[1],"|",bord[2])
    print (bord[3],"|",bord[4],"|",bord[5])
    print (bord[6],"|",bord[7],"|",bord[8])
def  check(char,spot1,spot2,spot3):
    if bord[spot1]==char and bord[spot2]==char and bord[spot3]==char:
        return True
def checkall(char):
    if check(char , 0, 1 , 2):
        return True
    if check(char,3,4,5):
        return True
    if check(char, 6, 7, 8):
        return True
    if check(char,0,4,8):
        return True
    if check(char,2,4,6):
        return True
    if check(char,0,3,6):
        return True
    if check(char,1,4,7):
        return True
    if check(char,2,5,8):
        return True
while True :
    pos=input("enter the position")
    pos=int(pos)-1
    if bord[pos] !="x" and bord[pos] != "o":
        bord[pos]="x"
        if checkall("x")==True:
            display_bord()
            print("x win")
            break
        while True:
            opp=random.randint(0,8)
            if bord[opp] !="o" and bord[opp] !="x":
                bord[opp]="o"
                if checkall("o")==True:
                    display_bord()
                    print("o win")
                   # break
                break
    else:
        print("position is taken")
    display_bord()