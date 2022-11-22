
from unittest import TestCase
from module import sqrt

class TestSqrt(TestCase):
    def test_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_one(self):
        self.assertEqual(sqrt(1), 1)

    def test_four(self):
        self.assertAlmostEqual(sqrt(4),2,5)


