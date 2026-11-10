from graphics import rectangle, circle 
from graphics.t3D_graphics import cuboid, sphere

print("Rectangle area:", rectangle.area (10,5))
print("Rectangle perimeter:", rectangle.peri(10,5))

print("Circle area:",circle.area(7))
print("Circle perimeter:",circle.perimeter(7))


print("Cuboid Surface area:",cuboid.surface_area(2,3,4))
print("Cuboid perimeter:",cuboid.perimeter(2,3,4))


print("Sphere surface area:",sphere.surface_area(5))
print("Sphere volume:",sphere.volume(5))