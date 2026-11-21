import unittest

from pilot import slugify, word_count


class SlugifyTests(unittest.TestCase):
    def test_lowercases_and_hyphenates(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_strips_edge_separators(self):
        self.assertEqual(slugify("  Phalanx! "), "phalanx")


class WordCountTests(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two  three"), 3)

    def test_empty(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()
