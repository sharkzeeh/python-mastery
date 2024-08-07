# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_bad_attribute(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 100


if __name__ == '__main__':
    unittest.main()
