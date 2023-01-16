import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    This will test translation from english to french
    """
    def test1(self):
        self.assertEqual(english_to_french(''), '') # test when null is given as input.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(english_to_french('Good morning'), 'Salut') # test when 'Hello' is given as input the output is not 'Hello'.

class TestfrenchToEnglish(unittest.TestCase):
    """
    This will test translation from french to english
    """
    def test1(self):
        self.assertEqual(french_to_english(''), '') # test when null is given as input.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertNotEqual(french_to_english('Salut'), 'Good morning') # test when 'Bonjour' is given as input the output is not 'Bonjour'.

if __name__ == '__main__':
    unittest.main()