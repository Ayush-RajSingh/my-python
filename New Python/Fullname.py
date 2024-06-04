def getFullName(f,m,l):
    f = f + m + l
    return f
    pass

def main():
    f = (input("enter your first name"))
    m = (input("enter your middle name"))
    l = (input("enter your last name"))
    n=getFullName(f,m,l)
    print("your full name is ",n)
pass
main()