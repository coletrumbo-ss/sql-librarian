from unittest.mock import patch
from unittest import TestCase
import unittest
import administrator

def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class TestAdminBranches(TestCase):

    # get_input will return 'yes' during this test
    @patch('yourmodule.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('yourmodule.get_input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')

if __name__ == '__main__':
    unittest.main()