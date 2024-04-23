class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <=0:
            raise ValueError(f'Width must be positive')
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <=0:
            raise ValueError(f'Width must be positive')
        else:
            self._height = height
    def area(self):
        return self.width*self.height
    
    def perimert(self):
        return 2 * (self.width + self.height)
    
    # def to_string(self):
    #     return f'Rectangle: width = {self.width}, height = {self.height}'

    def __str__(self):
        return f'Rectangle: width = {self.width}, height = {self.height}'
    
    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Rectangle):
            return self.width == value.width and self.height == value.height
        else:
            return False

    def __lt__(self, other: object):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


if __name__ == "__main__":
    r1 = Rectangle(10,20)
    r2 = Rectangle(10, 20)
    result = r1.area()
    perimeter = r1.perimert()
    print(f"The area of width {r1.width} and height {r1.height} is {result}")
    print(f"The perimeter of width {r1.width} and height {r1.height} is {perimeter}")
    print(f"the mem address for instance r1 is {r1}, mem address: {hex(id(r1))}")
    print("*******************************")
    print(r1)
    print(f'Is r1 == r2? {r1 == r2}')
    print(f'Is r1 == 100? {r1 == 100}')
    
    r3 = Rectangle(10,20)
    r4 = Rectangle(100, 200)
    print(f'Is r3 < r4? {r3 < r4}')
    