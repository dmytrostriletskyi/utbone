"""
Tests for
"""
from ddt import ddt, data, unpack
from mock import patch

from django.test import TestCase


class Test(TestCase):
    """
    Tests for
    """

    def setUp(self):
        """
        Initialize
        """
        pass

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
