import unittest
from BTCInput import *
import pickle

class TestStockItem(unittest.TestCase):
    
    def test_init(self):
        item = StockItem('REF123', 10.0, 'red', 'London')
        self.assertEqual(item.stock_ref, 'REF123')
        self.assertEqual(item.price, 10.0)
        self.assertEqual(item.color, 'red')
        self.assertEqual(item.location, 'London')
        self.assertEqual(item.stock_level, 0)
        self.assertEqual(item.item_name, 'Stock Item')
        self.assertEqual(item.StockItem_version, 1)
        
    def test_add_stock(self):
        item = StockItem('REF123', 10.0, 'red', 'London')
        item.add_stock(20)
        self.assertEqual(item.stock_level, 20)
        item.add_stock(30)
        self.assertEqual(item.stock_level, 50)
        with self.assertRaises(Exception):
            item.add_stock(-5)
        with self.assertRaises(Exception):
            item.add_stock(60)
            
    def test_sell_stock(self):
        item = StockItem('REF123', 10.0, 'red', 'London')
        item.add_stock(50)
        item.sell_stock(20)
        self.assertEqual(item.stock_level, 30)
        with self.assertRaises(Exception):
            item.sell_stock(40)
        with self.assertRaises(Exception):
            item.sell_stock(0)
        with self.assertRaises(Exception):
            item.sell_stock(-5)
            
    def test_set_price(self):
        item = StockItem('REF123', 10.0, 'red', 'London')
        item.set_price(15.0)
        self.assertEqual(item.price, 15.0)
        with self.assertRaises(Exception):
            item.set_price(0.2)
        with self.assertRaises(Exception):
            item.set_price(700.0)
            
    def test_str(self):
        item = StockItem('REF123', 10.0, 'red', 'London')
        item.add_stock(50)
        expected = '''Stock Reference: REF123
Type: Stock Item
Location: London
Price: 10.0
Stock level: 50
Color: red'''
        self.assertEqual(str(item), expected)


class TestDress(unittest.TestCase):
    
    def test_init(self):
        dress = Dress('REF456', 20.0, 'blue', 'floral', 'M', 'Paris')
        self.assertEqual(dress.stock_ref, 'REF456')
        self.assertEqual(dress.price, 20.0)
        self.assertEqual(dress.color, 'blue')
        self.assertEqual(dress.location, 'Paris')
        self.assertEqual(dress.stock_level, 0)
        self.assertEqual(dress.pattern, 'floral')
        self.assertEqual(dress.size, 'M')
        self.assertEqual(dress.item_name, 'Dress')
        self.assertEqual(dress.Dress_version, 1)
        
    def test_add_stock(self):
        dress = Dress('REF456', 20.0, 'blue', 'floral', 'M', 'Paris')
        dress.add_stock(20)
        self.assertEqual(dress.stock_level, 20)
        dress.add_stock(30)
        self.assertEqual(dress.stock_level, 50)
        with self.assertRaises(Exception):
            dress.add_stock(-5)
        with self.assertRaises(Exception):
            dress.add_stock(60)
            
    def test_sell_stock(self):
        dress = Dress('REF456', 20.0, 'blue', 'floral', 'M', 'Paris')
        dress.add_stock(50)
       