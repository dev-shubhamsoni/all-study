"""
Open/Closed Principle - Open for extension, closed for modification.

This principle states that Software entities (classes, modules, functions, etc.) should be open for extension, but closed for 
modification which means you should be able to extend a class behavior, without modifying it.

Why it matters:
• Prevents breaking existing code.
• Encourages reusable components.

"""

class Shape:
    def __init__(self, type):
        self.type = type

    def calculateArea(self):
        if self.type == "circle":
            # Circle area calculation
            pass
        elif self.type == "rectangle":
            # Rectangle area calculation
            pass
        # Adding a triangle requires modifying this method
        
"""

What's the problem?
Whenever you introduce a new shape, such as a triangle, you must modify calculateArea() by adding another if/elif condition.
This can make the code harder to maintain and increases the risk of breaking existing functionality.

Go with Open/Closed Principle
Better approach: Use polymorphism
Each shape should implement its own area calculation.

"""

import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement calculate_area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(4, 3)
]

for shape in shapes:
    print(shape.calculate_area())
    
"""

Explanation:
 In the corrected code example, each shape class has a single responsibility:

• Base Class (Shape): This is an abstract base class with an abstract function calculateArea(). It defines a common interface for all shapes.

• Circle Class: This class implements the calculateArea() logic for circles.

• Rectangle Class: This class implements the calculateArea() logic for rectangles.

• Triangle Class: This class implements the calculateArea() logic for triangles.

By adhering to the Open/Closed Principle, the code becomes more maintainable and easier to understand. Adding a new shape, like a 
triangle, does not require modifying the existing code. Instead, we extend the Shape class by creating a new class for the triangle. 
This approach prevents breaking existing code and encourages the creation of reusable components.


"""