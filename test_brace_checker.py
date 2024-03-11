import unittest

class TestIsValidParentheses(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(is_valid_parentheses("()"), (True, -1))
        self.assertEqual(is_valid_parentheses("()[]{}"), (True, -1))
        self.assertEqual(is_valid_parentheses("{[]}"), (True, -1))

    def test_invalid(self):
        self.assertEqual(is_valid_parentheses("(]"), (False, 1))
        self.assertEqual(is_valid_parentheses("([)]"), (False, 2))
        self.assertEqual(is_valid_parentheses("{[}]"), (False, 2))

if __name__ == "__main__":
    unittest.main()
