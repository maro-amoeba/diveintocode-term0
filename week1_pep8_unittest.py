import unittest
from pep8 import date_decision

class Testpep8(unittest.TestCase):
    """test class of pep8.py
    """

    def test_pep8(self):
        """test method for date_decision
        """

        value = "01/27 24:30"
        expected = "01/28 00:30"
        actual = date_decision(value)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
