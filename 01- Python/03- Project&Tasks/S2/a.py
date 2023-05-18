
def ConverToBinary(x):
    global num 
    if x >=1 :
        ConverToBinary(x//2)
    
    num = str(x%2) + num  


def NumberOfOnesInBinaryNumber(x):
    global num 
    num = ''  
    ConverToBinary(x)
    num = list(num)
    ones = 0 
    for i in range(0,len(num)):
        if num[i] == "1":
            ones+=1
    
    print("Number of ones = ",ones)


NumberOfOnesInBinaryNumber(5)
NumberOfOnesInBinaryNumber(0)
NumberOfOnesInBinaryNumber(2)

