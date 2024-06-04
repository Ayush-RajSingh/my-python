def factorial():
    num = int(input("Enter a number "))
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fact = fact*i
            print("The factorial of",num,"is",fact) 
def reverse():

    num1 = int(input("Enter a number: "))
    print(str(num1)[::-1])

def main():
    num2  = int(input("1.Factorial\n2.reverse\n"))

    if(num2 == 1):
        factorial()
    elif(num2 == 2):
        reverse()
    else:
        print("invalid choice")
main()