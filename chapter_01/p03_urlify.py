# O(N)
import unittest


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    string = string.strip()
    char_list = list(string)
    space_count = len(string.split(" ")) - 1
    # add two to the length per space to fix '%' '2' '0'
    new_index = len(char_list) + space_count * 2
    new_char_list = [''] * new_index

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            new_char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            new_char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(new_char_list[new_index:])


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.strip().replace(" ", "%20")


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
        ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
        ("", 0, ""),
        ("   ", 0, ""),
        (" a quick brown fox ", 17,  "a%20quick%20brown%20fox")
    ]
    testable_functions = [urlify_algo, urlify_pythonic]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for test_string, length, expected in self.test_cases:
                actual = urlify(test_string, length)
                assert actual == expected, \
                    f"{urlify.__name__} failed case: {test_string} -> {expected}, actual {actual}"


if __name__ == "__main__":
    unittest.main()
