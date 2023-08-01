import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 026 Skipped')
class TestIsAStringAPalindrome(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.026-is-a-string-a-palindrome.python.main'

    @patch('builtins.input')
    def test_ok_palindrome(self, mock_input):
        """
        Check if return the expected output
        """

        palindromes = ['bib', 'nun', 'madam', 'racecar', 'civic', 'deified', 'hannah', 'level', 'minim', 'mom', 'noon',
                       'radar', 'refer', 'rotator', 'sagas', 'solos', 'pop', 'peep', 'sis', 'redder', 'kayak', 'stats',
                       'dewed', 'tenet', 'wow']

        for word in palindromes:
            mock_input.return_value = word

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue().lower()
            self.assertIn('is a palindrome', result)

    @patch('builtins.input')
    def test_ok_not_palindrome(self, mock_input):
        """
        Check if return the expected output
        """

        palindromes = ['cat', 'base', 'blue', 'company', 'design', 'evening']

        for word in palindromes:
            mock_input.return_value = word

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue().lower()
            self.assertIn('not a palindrome', result)
