class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError(f'Width cannot be negative')
        else:
            self._width = width
            
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError(f'Height cannot be negative')
        else:
            self._height = height
            

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return  2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle: width = {self.width}, height = {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

if __name__ == "__main__":
    r1 = Rectangle(10,20)
    r2 = Rectangle(10,20)
    r3 = Rectangle(10,20)
    r4 = Rectangle(100,200)
    print(f'The area of a Rectangle with width {r1.width} and height {r1.height} is {r1.area()} ')
    print(f'The Perimeter of a Rectangle with width {r1.width} and height {r1.height} is {r1.perimeter()} ') 
    print(f'This is r1 {r1} ')
    print(f'Is r1 == r2? {r1 == r2}')
    print(f'Is r1 == 100? {r1 == 100}')
    

    
	



