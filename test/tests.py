import unittest
from main import is_valid_input


class TestPlayerMachineInteraction(unittest.TestCase):
    """ communication player / Jeu"""

    def test_strict_valid_direction_input(self):
        strict_valid_direction_values = ['n', 'o', 's', 'e']
        for value in strict_valid_direction_values:
            self.assertTrue(is_valid_input(value))

    def test_case_sensitive_direction_input(self):
        case_sensitive_valid_values = ['N', 'O', 'S', 'E']
        for value in case_sensitive_valid_values:
            self.assertTrue(is_valid_input(value))

    def test_number_before_direction_value_input(self):
        number_before_direction_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 1]
        for value in number_before_direction_values:
            self.assertFalse(is_valid_input(value))

    def test_not_valid_value_input(self):
        not_valid_values = ['a', '&']
        for value in not_valid_values:
            self.assertFalse(is_valid_input(value))

    def test_long_valid_value_input(self):
        long_valid_values = ['n1', 'e2', 's3', 'o4', 'N5', 'E6', 'S7', 'O8', 'N23', 'S408']
        for value in long_valid_values:
            self.assertTrue(is_valid_input(value))

    def test_long_unvalid_value_input(self):
        long_not_valid_values = ['na', 'be', 'c3']
        for value in long_not_valid_values:
            self.assertFalse(is_valid_input(value))

    def test_double_direction_value_input(self):
        valid_values_but_cant_be_together = ['nn', '11']
        for value in valid_values_but_cant_be_together:
            self.assertFalse(is_valid_input(value))
