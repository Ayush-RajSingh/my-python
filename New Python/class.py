class taX:
    
    def read(self):
        self.sal = int(input("Enter your salary"))

    def getTax(self):
        if (self.sal >= 500000):
            self.d=(10 * self.sal) % 100.0
        else:
            self.d=print("you can commit  tax fraud ")
    
    def show(self):
        print("Your tax will be ",self.d)

if __name__ == '__main__':
    t = taX()
    t.read()
    t.getTax()
    t.show()