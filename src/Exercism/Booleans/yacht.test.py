from ast import main
import unittest
import yacht


class yachtTest(unittest.TestCase):
    def MyTeSt(self):
        self.assertEqual(yacht.score([1, 1, 1, 4, 6], yacht.ONES), 3)

    def mytest2(self):
        self.assertEqual(yacht.score([1, 1, 1, 1, 1, 1]), yacht.FIVES)


if __name__ == "__main__":
    unittest.main()
