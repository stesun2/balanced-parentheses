import unittest
from balance_parens import balance_parens

class BalanceParensTestCase(unittest.TestCase):
    """Test for balance_parens.py"""

    def test_returns_empty_list(self):
        """Calls balance_parens.py, returns an empty list"""
        self.assertEqual()
    
    def test_returns_min_size(self):
        """Calls balance_parens.py, returns the length of min size """
        self.assertEqual()

    def test_returns_padded_list(self):
        """Calls balance_parens.py, returns a padded list mode"""
        self.assertEqual()

    def test_returns_non_negative_int(self):
        """Calls balance_parens.py, checks if min_size is non-negative integer"""
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()

# # Add more test cases!...
# print(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
# print(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")

# # Challenge: nested parentheses...
# print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")

# balanceParens("()") # should return "()"
# balanceParens("a(b)c)") # should return "a(b)c"
# balanceParens("(a)(bdd)c)") # should return "(a)(bdd)c"
# balanceParens("a(dbvb)c)") # should return "a(dbvb)c"
# balanceParens("a(b)(c)())") # should return "a(b)(c)()"
# balanceParens(")(") # should return ""
# balanceParens("(((((") # should return ""
# balanceParens(")(())(") # should return "(())"
# balanceParens("(()()(") # should return "()()"
# balanceParens(")())(()()(") # should return "()()()"