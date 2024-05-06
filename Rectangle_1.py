class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <=0:
            raise ValueError('Width cannot be zero')
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <=0:
            raise ValueError('Height cannpt be less or equal to zero')
        else:
            self._height = value
            
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.height + self.width)

    def __repr__(self):
        return f'Rectangle ({self.width}, {self.height})'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            return False


if __name__ == "__main__":
    r1 = Rectangle(20,10)
    r2 = Rectangle(20,10)
    r1_area = r1.area()
    r1_area = r1.perimeter()
    print(f'R1 {r1}')
    print(f'R2 {r2}')
    print(f'Is R1 == R2? {r1 == r2}')
    print(f'Is R1 == 100? {r1 == 100}')
