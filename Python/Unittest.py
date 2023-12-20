
import unittest
if __name__ == '__main__':
    unittest.main()
from stock_item import Dress

class TestDress(unittest.TestCase):

    # Test 1: Check that a Dress object can be initialized with the correct attributes.
    def test_dress_init(self):
        dress = Dress('ABC123', 50.0, 'red', 'floral', 'M', 'London')
        self.assertEqual(dress.stock_ref, 'ABC123')
        self.assertEqual(dress.price, 50.0)
        self.assertEqual(dress.color, 'red')
        self.assertEqual(dress.pattern, 'floral')
        self.assertEqual(dress.size, 'M')
        self.assertEqual(dress.location, 'London')
        self.assertEqual(dress.stock_level, 0)
        self.assertEqual(dress.item_name, 'Dress')
        self.assertEqual(dress.Dress_version, 1)

    # Test 2: Check that stock can be added to a Dress object.
    def test_add_stock(self):
        dress = Dress('ABC123', 50.0, 'red', 'floral', 'M', 'London')
        dress.add_stock(10)
        self.assertEqual(dress.stock_level, 10)
        dress.add_stock(20)
        self.assertEqual(dress.stock_level, 30)
        with self.assertRaises(Exception):
            dress.add_stock(-5)
        with self.assertRaises(Exception):
            dress.add_stock(100)

    # Test 3: Check that stock can be sold from a Dress object.
    def test_sell_stock(self):
        dress = Dress('ABC123', 50.0, 'red', 'floral', 'M', 'London')
        dress.add_stock(10)
        dress.sell_stock(5)
        self.assertEqual(dress.stock_level, 5)
        with self.assertRaises(Exception):
            dress.sell_stock(6)
        with self.assertRaises(Exception):
            dress.sell_stock(-2)
        with self.assertRaises(Exception):
            dress.sell_stock(0)

    # Test 4: Check that the string representation of a Dress object is formatted correctly.
    def test_str(self):
        dress = Dress('ABC123', 50.0, 'red', 'floral', 'M', 'London')
        dress.add_stock(10)
        expected = 'Stock Reference: ABC123\nType: Dress\nLocation: London\nPrice: 50.0\nStock level: 10\nColor: red\nPattern: floral\nSize: M'
        self.assertEqual(str(dress), expected)
