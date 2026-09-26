import unittest
from challenge import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_basic_word(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_uppercase_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case_and_spaces(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            count_vowels(12345)
