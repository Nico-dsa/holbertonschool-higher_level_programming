#!/usr/bin/python3
"""Function that write a class Rectangle that defines a rectangle """


class Rectangle:
    """Defines rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
        """width: width of side of the rectangle"""
        """height: height of the rectangle"""

    @property
    def width(self):
        """Property for the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            """Value: widht value to set"""
            """TypeError: if width is not an integer"""
            """ValueError: if width < 0 """
        self.__width = value

    @property
    def height(self):
        """Property for the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            """Value: height value to set"""
            """TypeError: if width is not an integer"""
            """ValueError: if width < 0 """
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for i in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """return a string representation of the rectangle\
        to be able to recreate a new instance"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print the message Bye rectangle... \
        when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
