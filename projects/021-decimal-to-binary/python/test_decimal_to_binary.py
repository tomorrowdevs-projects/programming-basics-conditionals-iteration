import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 021 Skipped')
class TestDecimalToBinary(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.021-decimal-to-binary.python.main'

    @patch('builtins.input')
    def test_0_to_10_ok(self, mock_input):
        """
        Check if return the expected output
        """

        number_and_result = {'1': '1', '2': '10', '3': '11', '4': '100',
                             '5': '101', '6': '110', '7': '111', '8': '1000', '9': '1001', '10': '1010'}

        for number, ok_result in number_and_result.items():

            mock_input.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue().lower()
                self.assertIn(ok_result, result, f'The Binary of the Decimal {number} is {ok_result}')
