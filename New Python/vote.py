def readage():
    age=int(input("enter age"))
    return age
def show(age):
    if(age>=18):
        print("you can vote for modi now ")
    else:
        print("you can die")
def main():
    age=readage()
    show(age)
main()
