import unittest

from pilot import clamp, mean
from pilot.numbers import median


class ClampTests(unittest.TestCase):
    def test_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_limits(self):
        self.assertEqual(clamp(-1, 0, 10), 0)
        self.assertEqual(clamp(11, 0, 10), 10)

    def test_rejects_inverted_range(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


class MeanTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            mean([])


class MedianTests(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(median([1, 2, 3]), 2)

    def test_even_count(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_unsorted(self):
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
