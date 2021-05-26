"""Tests for task01 - File&Errors"""
import os
import unittest
from os.path import exists

from homework4.task01 import is_number_in_interval


class InitTest(unittest.TestCase):
    file = None

    def setUp(self):
        self.file = open("my_file.txt", "w+")

    def test_negative_opening(self):
        try:
            open("my_file.txt")
        except Exception as x:
            self.assertIsInstance(x, FileNotFoundError)

    def test_positive_opening(self):
        self.assertTrue(exists("my_file.txt"))

    def test_file_is_empty(self):
        try:
            open("my_file.txt", "w+")
            self.file.close()
        except Exception as x:
            self.assertIsInstance(x, ValueError)

    def test_first_num_is_in_interval(self):
        first_string = "2"
        self.file.write(first_string)
        self.file.close()
        self.assertTrue(is_number_in_interval("my_file.txt"))

    def test_first_num_is_not_in_interval(self):
        first_string = "4"
        self.file.write(first_string)
        self.file.close()
        self.assertFalse(is_number_in_interval("my_file.txt"))

    def test_string_is_not_number(self):
        try:
            open("my_file.txt", "w+")
            first_string = "None"
            self.file.write(first_string)
            self.file.close()
        except Exception as x:
            self.assertIsInstance(x, ValueError)

    def tearDown(self):
        self.file.close()
        os.remove("my_file.txt")
