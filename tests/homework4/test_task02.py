"""Test for task02 - URL"""
import unittest
from unittest.mock import MagicMock
from urllib import request

from homework4.task02 import count_dots_on_i


class InitTest(unittest.TestCase):
    def test_count_dots_on_i(self):
        url = "http://www.example.com"
        count_dots_on_i = MagicMock(return_value=10)
        self.assertEqual(count_dots_on_i(url), 10)

    def test_count_dots_with_exception(self):
        url = "http://www.example.com"
        request.urlopen = MagicMock(side_effect=ConnectionError)
        with self.assertRaises(ValueError, msg=f"Unreachable {url}"):
            count_dots_on_i(url)


if __name__ == "__main__":
    unittest.main()
