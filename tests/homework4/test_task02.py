"""Test for task02_var1 - URL"""
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch
from urllib import request

from homework4 import task02_var1
from homework4.task02_var1 import count_dots_on_i1


class TestFunc1(TestCase):
    def test_count_i1_where_i_exists(self):
        with patch.object(task02_var1, "urlopen", return_value=Mock()) as urlopen_mock:
            mock_response_read = Mock()
            urlopen_mock.return_value.read = mock_response_read
            mock_response_read.return_value = b"iii"
            assert count_dots_on_i1("test_get_data") == 3

    def test_count_i1_where_i_does_not_exist(self):
        with patch.object(task02_var1, "urlopen", return_value=Mock()) as urlopen_mock:
            mock_response_read = Mock()
            urlopen_mock.return_value.read = mock_response_read
            mock_response_read.return_value = b"not"
            assert count_dots_on_i1("test_get_data") == 0

    def test_count_dots1_with_exception(self):
        url = "no_link"
        request.urlopen = MagicMock(side_effect=ConnectionError)
        with self.assertRaises(ValueError, msg=f"Unreachable {url}"):
            count_dots_on_i1(url)
