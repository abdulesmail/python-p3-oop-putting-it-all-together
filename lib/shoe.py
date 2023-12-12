#!/usr/bin/env python3

class Shoe:
     def __init__(self, brand, size):
        self.brand = brand
        self._size = size  # Use a private attribute for size

     @property
     def size(self):
        return self._size

     @size.setter
     def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self._size = value

     def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

     def __str__(self):
        return f"Shoe(brand='{self.brand}', size={self.size}, condition='{self.condition}')"
     pass