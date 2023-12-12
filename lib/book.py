#!/usr/bin/env python3

class Book:
       def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

       def turn_page(self):
        print("Flipping the page...wow, you read fast!")

       def __str__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"
pass
