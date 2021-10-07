import unittest


class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class CalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.calculator = Calculator()

    def tearDown(self):
        print('tearDown')

    def test_add(self):
        self.assertEqual(2, self.calculator.add(1, 1))

    def test_sub(self):
        self.assertEqual(-8, self.calculator.sub(2, 10))

    def test_mul(self):
        self.assertEqual(9449772114007, self.calculator.mul(1234567, 7654321))

    def test_div(self):
        self.assertEqual(2.5, self.calculator.div(10, 4))

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            self.calculator.div(1, 0)
        print(cm.exception)
