import unittest

class TestStrings(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('foo'.upper() == 'FOO')
        #self.assertEqual('foo'.upper(), "Foo")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__': # only run if this script is invoked from the command-line:
    unittest.main()
