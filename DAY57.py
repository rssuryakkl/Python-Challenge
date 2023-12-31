#Hii all This is DAY57(31-12-2023) today's topic is ATM Program
#ATM Mini ATM machine
pin=8265
amount=1000
user_pin=int(input("Enter Your Pin Number:"))
if user_pin == pin:
    print("1.Deposit\n2.Withdraw\n3.Balance Enquiry")
    ch = int(input("Enter your Choice:"))
    if ch ==1:
        Depamount=int(input("Enter The Amount to be Deposit:"))
        amount=amount+Depamount
        print("Your aviliable balance:",amount)
    elif ch == 2:
        Withamount=int(input("Enter a Amount to be Withdraw:"))
        if amount<Withamount:
            print("Insufficient Balance")
        else:
            amount=amount-Withamount
            print("Your aviliable balance:",amount)
    elif ch == 3:
        print("Your aviliable balance:",amount)
    else:
        print("Wrong Input")
else:
    print("Please enter correct PIN Number")
