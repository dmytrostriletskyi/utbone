"""
Tests for
"""
import unittest
from ddt import ddt, data, unpack
from mock import patch


class Test(unittest.TestCase):
    """
    Tests for
    """

    def test_first(self):
        """
        Verify that
        """
        self.assertEqual(1, '1')

    @patch('')
    def test_second(self, mock_):
        """
        Assert that
        """
        pass

    @data(
        ('first', 'second', 'expected'),
        ('first', 'second', 'expected'),
    )
    @unpack
    def test_third(self, first, second, expected):
        """
        Make sure when
        """
        pass


if __name__ == '__main__':
    unittest.main()
