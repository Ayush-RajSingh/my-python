def area(n1,n2)->float :
    n3 = 2 * (n1+n2)
    return n3

def printans(n3):
    n4 = print("area of rectangle is ",n3)
    return n4
    

def main():
    n1 = float(input("ENTTER N1"))
    n2 = float(input("ENTER N2"))
    n3 = area(n1,n2)
    n4 = printans()
    
main()