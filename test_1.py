"""CS 1001 - Lab Programming 5: starter unit tests.

Starter tests intentionally fail with NotImplementedError until you
complete day1.py. Add MULTIPLE additional tests for EACH function:
empty lists, one-element lists, negative/zero values, ties, and original
object identity where appropriate. Use self.assertEqual, not bare assert.

Run with: python -m unittest test_1.py
"""

import unittest

from day1 import (
    Point,
    Book,
    count_positive,
    sum_x_coordinates,
    average_y_coordinate,
    book_with_most_authors,
    furthest_from_origin,
    closest_book_title,
)


class TestProvidedDataClasses(unittest.TestCase):
    def test_point_and_book_construction(self):
        p = Point(3.0, 4.0)
        book = Book(["Author A", "Author B"], "Example")
        self.assertEqual(3.0, p.x)
        self.assertEqual(4.0, p.y)
        self.assertEqual(["Author A", "Author B"], book.authors)
        self.assertEqual("Example", book.title)

    def test_provided_point_distance(self):
        self.assertEqual(5.0, Point(0, 0).distance_to(Point(3, 4)))


class TestCountPositive(unittest.TestCase):
    def test_mixed_signs(self):
        self.assertEqual(3, count_positive([-3, 5, 0, -1, 8, 2]))

    def test_empty(self):
        self.assertEqual(0, count_positive([]))

    # TODO: Add additional tests for only-positive, only-nonpositive, etc.


class TestSumXCoordinates(unittest.TestCase):
    def test_multiple_points(self):
        points = [Point(1.0, 4.0), Point(3.0, 2.0), Point(-2.0, 8.0)]
        self.assertEqual(2.0, sum_x_coordinates(points))

    def test_empty(self):
        self.assertEqual(0.0, sum_x_coordinates([]))

    # TODO: Add additional tests for a single point, zeros, negatives.


class TestAverageYCoordinate(unittest.TestCase):
    def test_multiple_points(self):
        points = [Point(1, 2), Point(4, 6), Point(8, 10)]
        self.assertEqual(6.0, average_y_coordinate(points))

    def test_empty(self):
        self.assertEqual(None, average_y_coordinate([]))

    # TODO: Add additional tests for one point and negative values.


class TestBookWithMostAuthors(unittest.TestCase):
    def test_book_with_most_authors(self):
        first = Book(["Octavia E. Butler"], "Kindred")
        second = Book(["Malcolm X", "Alex Haley"], "The Autobiography of Malcolm X")
        third = Book(["Toni Morrison"], "Beloved")
        self.assertEqual(True, book_with_most_authors([first, second, third]) is second)

    def test_empty(self):
        self.assertEqual(None, book_with_most_authors([]))

    # TODO: Add tests for ties and identity of the returned Book object.


class TestFurthestFromOrigin(unittest.TestCase):
    def test_multiple_points(self):
        points = [Point(1, 1), Point(3, 4), Point(2, 2)]
        self.assertEqual(1, furthest_from_origin(points))

    def test_empty(self):
        self.assertEqual(None, furthest_from_origin([]))

    # TODO: Add tests for negative coordinates, ties, and one point.


class TestClosestBookTitle(unittest.TestCase):
    def test_closest_title(self):
        books = [
            Book(["Toni Morrison"], "Beloved"),
            Book(["Malcolm X", "Alex Haley"], "The Autobiography of Malcolm X"),
            Book(["Octavia E. Butler"], "Kindred"),
        ]
        # Beloved and Kindred each have seven letters, so first wins.
        self.assertEqual("Beloved", closest_book_title(books, 8))

    def test_empty(self):
        self.assertEqual(None, closest_book_title([], 8))

    # TODO: Add tests for exact matches, single books, and other ties.


if __name__ == "__main__":
    unittest.main()
