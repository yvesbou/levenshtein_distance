import unittest
from Levenshtein import Levenshtein_distance


class Test_Levenshtein(unittest.TestCase):
    def test_length0(self):
        result = Levenshtein_distance('Luca', '')
        true_result = len('Luca')
        self.assertEqual(true_result, result)

    def test_length_deletion(self):
        result = Levenshtein_distance('Luca', 'Luc')
        true_result = 1
        self.assertEqual(true_result, result)

    def test_length_insertion(self):
        result = Levenshtein_distance('Luca', 'Lucas')
        true_result = 1
        self.assertEqual(true_result, result)

    def test_length_substitution(self):
        result = Levenshtein_distance('Luca', 'Luka')
        true_result = 1
        self.assertEqual(true_result, result)

if __name__ == '__main__':
    unittest.main()
