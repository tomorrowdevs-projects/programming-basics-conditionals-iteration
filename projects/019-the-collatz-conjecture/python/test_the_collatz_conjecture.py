import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 019 Skipped')
class TestTheCollatzConjecture(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.019-the-collatz-conjecture.python.main'

    @patch('builtins.input')
    def test_positive_ok(self, mock_inputs):
        """
        Check if return the correct result
        """

        mock_inputs.side_effect = ['8', '2', '0']

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue()
            formatted_result = [x.lower() for x in result.split()]

            ok_result = ['8', '4', '2', '1', '2', '1']

            self.assertEqual(ok_result, formatted_result, 'Output different that the expected')

    @patch('builtins.input')
    def test_negative_ok(self, mock_inputs):
        """
        Check if return the correct result
        """

        mock_inputs.side_effect = ['-3', '0']

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue()
            formatted_result = [x.lower() for x in result.split('\n')]

            ok_result = ['']

            self.assertEqual(ok_result, formatted_result, 'Output different that the expected')
