import unittest
from glob import iglob

from techtest import find_squares, MapError


class TestExamples(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def solution(self, filepath):
        '''
        Opens the solution associated with a file, and returns its contents

        :param filepath: A path to an example file
        :type filepath: str or pathlib.Path
        :return: a list of strings which describes the expected return value
        for the given example
        :rtype: list[str]
        '''
        filepath = filepath.replace('examples', 'examples_solutions')

        with open(filepath, 'r') as f:
            data = [line.strip('\n') for line in f]
        return data

    def _test(self, path):
        self.assertEqual(find_squares(path), self.solution(path))

    def _error_test(self, path):
        with self.assertRaises(MapError) as cm:
            find_squares(path)
        self.assertEqual(str(cm.exception), self.solution(path)[0])

    def test_2_solutions(self):
        '''
        Test the case when a map has two (or more) solutions.
        The expected result is to choose the top-left most solution.
        '''
        self._test('examples/2_solutions.txt')

    def test_example_other_chars(self):
        '''
        Test the case when the describing characters are not ., o and x.

        In this example, they are replaced with -, ! and _ (respectfully)
        '''
        self._test('examples/example_-!_.txt')

    def test_example_082(self):
        '''Test the case when the describing characters are digits'''
        self._test('examples/example_082.txt')

    def test_example_solved(self):
        '''Test the case when the puzzle is already solved'''
        self._test('examples/example_solved.txt')

    def test_example(self):
        '''
        Test for the provided example in the technical test summary.
        '''
        self._test('examples/example.txt')

    def test_no_square(self):
        '''
        Test the case when there is no square
        to be found (all obstacles)
        '''
        self._test('examples/no_square.txt')

    def test_no_obstacle(self):
        '''Test the case when there is no obstacle to be found'''
        self._test('examples/no_obstacle.txt')

    def test_size_1(self):
        '''Test the case when the map is of size 1'''
        self._test('examples/size_1.txt')

    def test_error_characters_invalid(self):
        '''
        Test the case when the map is invalid because of the use of
        characters not in the metadata line.
        '''
        self._error_test('examples/error_charactersinvalid.txt')

    def test_error_line_inconsistent(self):
        '''
        Test the case when the map is invalid because some lines are longer
        than others
        '''
        self._error_test('examples/error_lineinconsistent.txt')

    def test_error_line_mismatch(self):
        '''
        Test the case when the map is invalid because the number of lines
        in the metadata is not the same as the number of lines in the map
        '''
        self._error_test('examples/error_linemismatch.txt')

    def test_error_no_lines(self):
        '''
        Test the case when the map is invalid because there is no map
        '''
        self._error_test('examples/error_0lines.txt')
