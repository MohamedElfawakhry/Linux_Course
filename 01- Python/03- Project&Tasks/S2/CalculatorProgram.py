
HexTable = { 0 : '0' , 1 : '1', 2 : '2',3 : '3',4 : '4',5 : '5',6 : '6',7 : '7',
            8 : '8',9 : '9',10 : 'A', 11 : 'B' ,  12 : 'C' ,13 : 'D', 14 : 'E',15 : 'F'  }
def Add(x , y):
    return x+y
def Sub(x,y):
    return x-y
def Mul(x,y):
    return x*y
def Div(x,y):
    return x/y

def ConverToBinary(x):
    if x >=1 :
        ConverToBinary(x//2)
    print(x%2,end="")
def ConvertToHex(decmiel):
    hexa = ''
    while(decmiel > 0):
        reminder = decmiel % 16 
        hexa = HexTable[reminder] + hexa
        decmiel = decmiel // 16
    return hexa 
while True:
    print("For Scintific Mode Enter  ==>  1")
    print("For Programmer Mode Enter ==>  2")
    mode = int(input())
    if mode == 1:
        print("="*100)
        print("\t\t\t\tYou'r in scientific mode ")
        print("="*100)
        x = ''
        while x != 'n' :
            num1 = int(input("Enter Number 1 : "))
            num2 = int(input("Enter Number 2 : "))

            operator = input("Enter The Operator ( + , - , * , /) :  ")

            if operator == "+" :
                print(num1 , " + ",num2," = ",Add(num1,num2))

            elif operator == "-" :
                print(num1 , " - ",num2," = ",Sub(num1,num2))

            elif operator == "*" :
                print(num1 , " * ",num2," = ",Mul(num1,num2))

            elif operator == "/" :
                print(num1 , " / ",num2," = ",Div(num1,num2))
            x = input("Do you want to continue ? (y/n)    ")
    elif mode == 2:
        x=""
        print("="*100)
        print("\t\t\t\tYou'r in Programmer mode ")
        print("="*100)

        while x != "0":
            print("To Convert to binary Enter       ==>  bin ")
            print("To Convert to hexa Enter         ==>  hex")
            print("To exit programmer mode enter    ==>  0")
            x = input()
            if x == "bin":
                num1 = int(input("Enter Decimel Number  : "))
                print("Number in binary = ",end="")
                ConverToBinary(num1)
                print()
            elif x== "hex":
                num1 = int(input("Enter Decimel Number  : "))
                print("Number in hexa = 0x",ConvertToHex(num1),end="")
                print()
