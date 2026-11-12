"""CS 1001 - Lab Programming 6: Strings and Mixed Data.

One-day lab: Friday, November 13, 2026.

Complete the six REQUIRED TODO functions below. Do not change any
function signatures, and do not provide solutions in test_1.py.
You may also attempt the optional histogram challenge.

Strings are immutable. Return new strings/lists where requested and do
not modify input lists. Write additional tests in test_1.py.
"""


def count_character(text: str, target: str) -> int:
    """Count occurrences of the one-character target in text.

    Case-sensitive. Example: count_character("banana", "a") -> 3.
    Do not use str.count().
    """
    # TODO (Task 1): Use a loop and an integer accumulator.
    raise NotImplementedError


def swap_case(text: str) -> str:
    """Return a new string with each letter's case reversed.

    Leave numbers, punctuation, and spaces unchanged.
    Example: swap_case("Hello World!") -> "hELLO wORLD!".
    Do not use str.swapcase().
    """
    # TODO (Task 2): Construct the result one character at a time.
    raise NotImplementedError


def str_translate(text: str, old: str, new: str) -> str:
    """Return text with every occurrence of old replaced by new.

    old and new are each exactly one character.
    Example: str_translate("abcdcba", "a", "x") -> "xbcdcbx".
    Do not use str.replace() or str.translate().
    """
    # TODO (Task 3): Build a new string without using replace().
    raise NotImplementedError


def remove_character(text: str, target: str) -> str:
    """Return text with every occurrence of target removed.

    target is exactly one character.
    Example: remove_character("mississippi", "s") -> "miiippi".
    Do not use str.replace().
    """
    # TODO (Task 4): Keep only characters that do not match target.
    raise NotImplementedError


def words_of_length(text: str, length: int) -> list[str]:
    """Return words of exactly the requested length, in original order.

    A word is a whitespace-separated token from text.split().
    Example: words_of_length("the quick brown fox", 3) -> ["the", "fox"].
    """
    # TODO (Task 5): Use split() and filter the resulting words.
    raise NotImplementedError


def groups_of_3(values: list[int]) -> list[list[int]]:
    """Group consecutive values into new sublists of at most 3 items.

    The last group can have 1 or 2 items; [] becomes [].
    Example: groups_of_3([1, 2, 3, 4]) -> [[1, 2, 3], [4]].
    Do not modify values.
    """
    # TODO (Task 6): Build a nested list, preserving input order.
    raise NotImplementedError


def histogram(text: str) -> dict[str, int]:
    """OPTIONAL CHALLENGE: Count each whitespace-separated word.

    Example: histogram("red blue red") -> {"red": 2, "blue": 1}.
    Return {} for an empty string. Do not use collections.Counter.
    Not required for signoff; no starter tests are provided for this.
    """
    # OPTIONAL TODO (Challenge): Build a dictionary of word counts.
    raise NotImplementedError
