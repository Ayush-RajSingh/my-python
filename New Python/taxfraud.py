def getTax(sal)->float:
    if (sal >= 500000):
        d=(10 * sal) % 100.0
    else:
        d=print("you can commit  tax fraud ")
    return d
pass
def main():
    sal = int(input("Enter your salary"))
    d = getTax(sal)
    print("Your tax will be ",d)
pass
main()