class A:
    def show(self):
        print("show")
        
class B:
    def display(self):
        print("display")

class C(A,B):
    def greeting(self):
        print("Hello")


if __name__ == '__main__':
    c = C()
    c.show()
    c.display()
    c.greeting()
    