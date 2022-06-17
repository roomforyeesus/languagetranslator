import unittest

from translator import englishToFrench, frenchToEnglish


class TestenglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()