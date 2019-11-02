import unittest
import rpn

class TestBasics(unittest.TestCase):
#    def test_add(self):
#        result = rpn.calculate("1 1 +")
#        self.assertEqual(2, result)
#    def test_sub(self):
#        result = rpn.calculate("1 1 -")
#        self.assertEqual(0, result)
#    def test_mul(self):
#        result = rpn.calculate("12 8 *")
#        self.assertEqual(96, result)
#    def test_badinput(self):
#        with self.assertRaises(TypeError):
#            rpn.calculate('1 2 3 +')
    def test_power(self):
        result = rpn.calculate("1 2 ^")
        self.assertEqual(1, result)
