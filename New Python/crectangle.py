class Rectangle:
    
    def read(self):
        self.l = float(input("Enter length "))
        self.b = float(input("Enter breadth "))
    
    def area(self):
        self.a = self.l * self.b
        print("area is ",self.a)
    
    def perimeter(self):
        self.p = 2*(self.l + self.b)
        print("perimter is ",self.p)

if __name__ == '__main__':
    r = Rectangle()
    r.read()
    r.area()
    r.perimeter()