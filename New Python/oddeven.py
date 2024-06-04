def isEven(num)->bool:
        if num % 2 == 0:
                return True
        else:
                return False
pass

def main():
    num = int(input("enter any number"))
    b = isEven(num)
    if(b == True ):
        print("even")
    else:
        print("odd")
    pass
main()