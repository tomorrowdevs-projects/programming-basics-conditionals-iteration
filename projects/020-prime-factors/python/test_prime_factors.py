import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 020 Skipped')
class TestPrimeFactors(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.020-prime-factors.python.main'

    @patch('builtins.input')
    def test_2_ok(self, mock_input):
        """
        Check if return the expected output
        """

        mock_input.return_value = '2'

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue().lower()
            self.assertIn('2', result)

    @patch('builtins.input')
    def test_10_ok(self, mock_input):
        """
        Check if return the expected output
        """

        mock_input.return_value = '10'

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue().lower()
            self.assertIn('2', result)
            self.assertIn('5', result)

