balance = 0
def readbalance():
    global balance
    balance=int(input("ENTER BALANCE"))

def withdraw():
    global balance
    amt=int(input("enter amount to withdraw"))
    balance = balance - amt 
    pass

def deposit():
    global balance 
    amt=int(input("enter the amount for deposit"))   
    balance = balance + amt 
    pass

def showbalance():
    global balance 
    print("your balance is ",balance)
    pass


def main():
    readbalance()
    num  = int(input("ENTER 1.WITHDRAW\n2.DEPOSIT\n"))
    if(num == 1):
        withdraw()
        showbalance()
    elif(num == 2):
        deposit()
    showbalance()
main()
