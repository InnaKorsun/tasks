import unittest
from year_triangle import year,triangle,triangletype

class YearTests(unittest.TestCase):
    def test_year_usual(self):
        actual_result = year(2018)
        self.assertEqual(actual_result, "False")

    def test_year_notusual(self):
        actual_result = year(2024)
        self.assertEqual(actual_result, "True")

class TriangleTest(unittest.TestCase):

    def test_triangle_positive(self):
        actual_result = triangle(3,3,3)
        self.assertEqual(actual_result,"True")

    def test_triangle_negative(self):
        actual_result = triangle(3,3,53)
        self.assertEqual(actual_result,"False")

class TriagleTypeTests(unittest.TestCase):

    def test_triangle_equilateral(self):
        actual_result = triangletype(3,3,3)
        self.assertEqual(actual_result,"Equilateral triangle")

    def test_triangle_isosceles(self):
        actual_result = triangletype(3,3,4)
        self.assertEqual(actual_result,"Isosceles triangle")

    def test_triangle_versatile(self):
        actual_result = triangletype(4,5,6)
        self.assertEqual(actual_result,"Versatile triangle")

    def test_not_triangle(self):
        actual_result = triangletype(3,3,53)
        self.assertEqual(actual_result,"Not a triangle")

if __name__=="__main__":
    unittest.main()
