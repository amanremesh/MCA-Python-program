class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle1 = rectangle(10, 20)
rectangle2 = rectangle(30, 40)

print("Area of first rectangle =", rectangle1.area())
print("Area of second rectangle =", rectangle2.area())

print("Perimeter of first rectangle =", rectangle1.perimeter())
print("Perimeter of second rectangle =", rectangle2.perimeter())

if rectangle1.area() > rectangle2.area():
    print("Area of rectangle1 is greater than area of rectangle2")
else:
    print("Area of rectangle2 is greater than area of rectangle1")
