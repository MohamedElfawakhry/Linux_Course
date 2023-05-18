from os import system , name
from time import sleep 


# DisplayClear Function
def Clear():
    system('cls')

def DrawRightArrowFunction():
    for i in range(5):
        print()
    for i in range(5):
        print("\t\t\t\t\t",end="")
        for k in range (i+1):
            print("*",end="")
        print()
    print("\t\t\t\t",end="")
    for line in range(14):
        print("*",end="")
    print()
    
    for i in range(5 , 0 , -1 ):
        print("\t\t\t\t\t",end="")
        for k in range(0 , i):
            print("*",end="")
        print()
def DrawLeftArrowFunction():
    
    for i in range(5):
        print()
    for k in range(0,5):
        print("\t\t   ",end="")
        for space in range(0,5-k):
            print(" ",end="")
        for i in range(0,k):
            print("*",end="")
        print()
    print("\t\t   ",end="")
    for line in range(14):
        print("*",end="")
    print()
    for k in range(0,6):
        print("\t\t   ",end="")
        for space in range(0,k):
            print(" ",end="")
        for i in range(0,6-k):
            print("*",end="")
        print()
    print()
def DrawDownArrowFunction():
    for i in range(10):
        print()
    for i in range(9):
        print("\t\t\t\t",end="")
        print("*",end="")
        print()
    for i in range(10 , 1 , -2):
        
        print("\t\t\t",end="")
        for space in range(0 , 10-i):
            print(" ",end="")
        for j in range(i ,2*i-1):
            print("*",end="")
        for j in range(1 , i-1):
            print("*",end="")
        print()
def DrawUpArrowFunction():
    
    for i in range(1,6):
        print("\t\t\t    ",end="")
        for space in range(1,6-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()


    for i in range(6):
        print("\t\t\t        ",end="")
        print("*",end="")
        print()
    
    

print("For CLK WISE Enter 1 ")
print("For Counter CLK WISE Enter 2")

x = int(input())
if x == 1:
    while True:
        DrawRightArrowFunction()
        sleep(0.5)
        Clear()
        DrawDownArrowFunction()
        sleep(0.5)
        Clear()
        DrawLeftArrowFunction()
        sleep(0.5)
        Clear()
        DrawUpArrowFunction()
        sleep(0.5)
        Clear()
elif x== 2:
    while True:
        DrawRightArrowFunction()
        sleep(0.5)
        Clear()
        DrawUpArrowFunction()
        sleep(0.5)
        Clear()
        DrawLeftArrowFunction()
        sleep(0.5)
        Clear()
        DrawDownArrowFunction()
        sleep(0.5)
        Clear()