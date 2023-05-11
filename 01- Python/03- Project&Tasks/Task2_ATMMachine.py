
# Define users accounts as a dictionary of lists (PIN , Balance)

Users_names = {
    1234    : "Mohamed" ,
    5678    : "Khaled"  ,
    1222    : "Body"    
}
Users_money = [ 50000 , 10000, 20000 ]
# Define a Tuple of transaction types
transaction_types = ("1. Withdrawal", "2. Fast Cash", "3. Balance Inquiry")

# Define a function

#################################
while True:
    PinCheck = int(input("Enter Your PIN  "))
    if PinCheck in Users_names.keys():
        index = list(Users_names).index(PinCheck)
        print(transaction_types)
        trans_id = int(input("Enter Number of Transaction : "))
        if(trans_id == 1):
            amount = int(input("Enter amount : "))
            if(amount < Users_money[index]):
                print("You'r Transcation done SUCCESSFULLY")
                Users_money[index] = Users_money[index] - amount 
            else:
                print("ERROR in amount")
        elif(trans_id == 2): #fast Cash
            print("1. 200")
            print("2. 500")
            print("3. 1000")
            fast_cash_id = int(input("Enter Number : "))
            if(fast_cash_id == 1):
                if(Users_money[index] > 200):
                    print("You'r Transcation done SUCCESSFULLY")
                    Users_money[index] = Users_money[index] - 200
            elif(fast_cash_id == 2):
                if(Users_money[index] > 500):
                    print("You'r Transcation done SUCCESSFULLY")
                    Users_money[index] = Users_money[index] - 500
            elif(fast_cash_id == 3):
                if(Users_money[index] > 1000):
                    print("You'r Transcation done SUCCESSFULLY")
                    Users_money[index] = Users_money[index] - 1000         
        elif(trans_id == 3): #balance unquiry 
            print("Your available amount = ",Users_money[index],"$")


    else:
        print("Wrong Id")