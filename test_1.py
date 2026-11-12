"""CS 1001 - Lab Programming 6: starter unit tests.

Required functions initially raise NotImplementedError; this is expected.
Add MULTIPLE new unittest tests for EACH of the six required functions.
Test empty inputs, repeated characters, case sensitivity, special
characters, order preservation, short final groups, and non-mutation.
Use self.assertEqual(...), not bare assert.

Run: python -m unittest test_1.py

The optional histogram challenge is not part of the required test suite.
"""

import unittest

from day1 import (
    count_character,
    swap_case,
    str_translate,
    remove_character,
    words_of_length,
    groups_of_3,
)


class TestCountCharacter(unittest.TestCase):
    def test_repeated_character(self):
        self.assertEqual(3, count_character("banana", "a"))

    def test_not_found(self):
        self.assertEqual(0, count_character("banana", "z"))

    # TODO: Add empty-string, first/last, and case-sensitive tests.


class TestSwapCase(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual("hELLO wORLD!", swap_case("Hello World!"))

    def test_nonletters_unchanged(self):
        self.assertEqual("123 !?", swap_case("123 !?"))

    # TODO: Add empty-string, all-upper/lower, and non-English tests.


class TestStrTranslate(unittest.TestCase):
    def test_multiple_occurrences(self):
        self.assertEqual("xbcdcbx", str_translate("abcdcba", "a", "x"))

    def test_no_match(self):
        self.assertEqual("hello", str_translate("hello", "z", "q"))

    # TODO: Add empty-string, first/last, and old == new tests.


class TestRemoveCharacter(unittest.TestCase):
    def test_repeated_character(self):
        self.assertEqual("miiippi", remove_character("mississippi", "s"))

    def test_target_absent(self):
        self.assertEqual("hello", remove_character("hello", "z"))

    # TODO: Add empty-string, all-matches, and boundary tests.


class TestWordsOfLength(unittest.TestCase):
    def test_multiple_matching_words(self):
        text = "the quick brown fox jumps over the dog"
        self.assertEqual(["the", "fox", "the", "dog"], words_of_length(text, 3))

    def test_no_matches(self):
        self.assertEqual([], words_of_length("hi hello", 4))

    # TODO: Add empty-string, repeated-word, and other-length tests.


class TestGroupsOf3(unittest.TestCase):
    def test_partial_final_group(self):
        self.assertEqual(
            [[1, 2, 3], [4, 5, 6], [7, 8]],
            groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]),
        )

    def test_empty_input(self):
        self.assertEqual([], groups_of_3([]))

    # TODO: Add 1, 2, 3, 4, 6, and 9-element inputs, plus mutation tests.


if __name__ == "__main__":
    unittest.main()
