#!/usr/bin/env python3

import pytest
from book import Book

import io
import sys

@pytest.fixture
def sample_book():
    return Book("Sample Book", 100)


class TestBook:
 Book("Sample Book", 100)

class TestBook:
    def test_has_title_and_page_count(self, sample_book):
        assert sample_book.page_count == 100
        assert sample_book.title == "Sample Book"

    def test_can_turn_page(self, sample_book):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        sample_book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
        pass

    class Book:
     def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"

