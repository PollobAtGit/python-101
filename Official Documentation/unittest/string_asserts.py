import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())
        
    def test_split(self):
        self.assertEqual('hello world'.split(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
