import unittest

from techtest.findsquares import parse_metadata


class TestMetadataParser(unittest.TestCase):
    def test_digits(self):
        self.assertEqual((10, '0', '4', '5'), parse_metadata('10045'))

    def test_regular_characters(self):
        self.assertEqual((10, '.', 'o', 'x'), parse_metadata('10.ox'))
