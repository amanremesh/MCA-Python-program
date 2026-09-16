area_square = lambda s: s * s
area_rectangle = lambda l, b: l * b
area_triangle = lambda b, h: 0.5 * b * h

s = float(input("Square side: "))
print("Square area:", area_square(s))

l = float(input("Rectangle length: "))
b = float(input("Rectangle breadth: "))
print("Rectangle area:", area_rectangle(l, b))

b = float(input("Triangle base: "))
h = float(input("Triangle height: "))
print("Triangle area:", area_triangle(b, h))
