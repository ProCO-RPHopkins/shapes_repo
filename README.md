Shape Class Hierarchy

- Explaining Purpose of Class Hierarchy Using Polymorphism and Inheritance Concepts -
The shape class hierarchy uses the same set of rules to represent different shapes. 
1. The abstract class (ABC) "shape" is used to define a common interface for all shapes. The abstract methods are 
    overridden by each shape subclass.
2. The abstract method is declared for the area and perimeter methods using the @abstractmethod decorator. This allows 
    the circle, rectangle, and triangle subclasses to override the abstract class with actual implementations, which are the specific formulas to find area and perimeter for each shape. 
3. Polymorphism allows the shape classes to uniformly share the same area and perimeter methods.
4. The derived circle, rectangle, and triangle subclasses inherit the color attributes and get_color and set_color
    methods from the shape base class.
------------------------------------------------------------------------------------------------------------------------
- Shape Classes, Attributes, and Methods -
    This section is AI generated and was used as a reference to write the previous section.
### 1. `Shape` (Base Class)
- **Attributes**:
    - `color` (string): The color of the shape.
- **Methods**:
    - `__init__(self, color)`: Constructor to initialize the shape with the given color.
    - `calculate_area(self)`: Abstract method to calculate the area of the shape (must be overridden by subclasses).
    - `calculate_perimeter(self)`: Abstract method to calculate the perimeter of the shape (must be overridden by subclasses).
    - `get_color(self)`: Method to retrieve the color of the shape.
    - `set_color(self, color)`: Method to set the color of the shape.

### 2. `Circle` (Derived Class)
- **Attributes**:
    - `radius` (float): The radius of the circle.
- **Methods**:
    - `__init__(self, color, radius)`: Constructor to initialize the circle with the given color and radius.
    - `calculate_area(self)`: Overrides the base class method to calculate the area of the circle (πr²).
    - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter (circumference) of the circle (2πr).

### 3. `Rectangle` (Derived Class)
- **Attributes**:
    - `length` (float): The length of the rectangle.
    - `width` (float): The width of the rectangle.
- **Methods**:
    - `__init__(self, color, length, width)`: Constructor to initialize the rectangle with the given color, length, and width.
    - `calculate_area(self)`: Overrides the base class method to calculate the area of the rectangle (length × width).
    - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter of the rectangle (2 × (length + width)).

### 4. `Triangle` (Derived Class)
- **Attributes**:
    - `side1` (float): The length of the first side of the triangle.
    - `side2` (float): The length of the second side of the triangle.
    - `side3` (float): The length of the third side of the triangle.
- **Methods**:
    - `__init__(self, color, side1, side2, side3)`: Constructor to initialize the triangle with the given color and side lengths.
    - `calculate_area(self)`: Overrides the base class method to calculate the area of the triangle using Heron's formula.
    - `calculate_perimeter(self)`: Overrides the base class method to calculate the perimeter of the triangle (side1 + side2 + side3).
------------------------------------------------------------------------------------------------------------------------
- Testing -
run -- python shapes.py --

- Terminal Output -
![alt text](<Screenshot (225).png>)

