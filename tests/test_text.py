import unittest

from pilot import slugify, truncate, word_count


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


class TruncateTests(unittest.TestCase):
    def test_short_text_unchanged(self):
        self.assertEqual(truncate("abc", 5), "abc")

    def test_exact_width_unchanged(self):
        self.assertEqual(truncate("abcde", 5), "abcde")

    def test_long_text_truncated_with_ellipsis(self):
        result = truncate("abcdefgh", 5)
        self.assertEqual(result, "abcd\u2026")
        self.assertEqual(len(result), 5)

    def test_uses_single_horizontal_ellipsis_character(self):
        result = truncate("hello world", 6)
        self.assertEqual(result[-1], "\N{HORIZONTAL ELLIPSIS}")
        self.assertEqual(ord(result[-1]), 0x2026)
        self.assertNotIn("...", result)

    def test_width_one(self):
        self.assertEqual(truncate("abc", 1), "\u2026")

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            truncate("abc", 0)


if __name__ == "__main__":
    unittest.main()
