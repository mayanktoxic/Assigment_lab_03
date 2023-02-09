class Shape:
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
class Rectangle(Shape):
    def __init__(self, length, width, color):
        Shape.__init__(self, color)
        self.length = length
        self.width = width
        
    def get_area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, base, height, color):
        Shape.__init__(self, color)
        self.base = base
        self.height = height
        
    def get_area(self):
        return 0.5 * self.base * self.height
    
rect = Rectangle(8, 20, "red")
tri = Triangle(10, 20, "blue")

print("Rectangle color: ", rect.get_color())
print("Rectangle area: ", rect.get_area())

print("Triangle color: ", tri.get_color())
print("Triangle area: ", tri.get_area())
