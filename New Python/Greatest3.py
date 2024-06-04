def greatest(a,b,c)->int:
    if (a >= b and a >= c):
        largest = a
        d = a
    elif (b >= a and b >= c):
        largest = b
        d = b
    else:
        largest = c
        d = c
    return d
pass

def main():
    a = int(input("ENTTER Number 1:-"))
    b = int(input("ENTER Number 2:-"))
    c = int(input("ENTTER Number 3:-"))
    d=greatest(a,b,c)
    print("The Greatest Number is:- ",d)
pass
main()