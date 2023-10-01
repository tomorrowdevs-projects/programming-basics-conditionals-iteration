import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 010 Skipped')
class TestRoulettePayouts(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.010-roulette-payouts.python.main'

    # Red

    @patch('random.choice')
    def test_ok_red_1_18_odd(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [1, 3, 5, 7, 9]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                expected = f'The spin resulted in {number} . . .\n' \
                           f'Pay {number}\n' \
                           f'Pay Red\n' \
                           f'Pay Odd\n' \
                           f'Pay 1 to 18'

                result = mock_print.getvalue()

                self.assertIn(expected, result, '\nOutput different that the expected!')

    @patch('random.choice')
    def test_ok_red_1_18_even(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [12, 14, 16, 18]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'The spin resulted in {number} . . .\n'
                              f'Pay {number}\n'
                              'Pay Red\n'
                              'Pay Even\n'
                              'Pay 1 to 18', result, 'Output different that the expected!')

    @patch('random.choice')
    def test_ok_red_19_36_odd(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [19, 21, 23, 25, 27]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'The spin resulted in {number} . . .\n'
                              f'Pay {number}\n'
                              'Pay Red\n'
                              'Pay Odd\n'
                              'Pay 19 to 36', result, 'Output different that the expected')

    @patch('random.choice')
    def test_ok_red_19_36_even(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [30, 32, 34, 36]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'The spin resulted in {number} . . .\n'
                              f'Pay {number}\n'
                              'Pay Red\n'
                              'Pay Even\n'
                              'Pay 19 to 36', result, 'Output different that the expected')

    # Black

    @patch('random.choice')
    def test_ok_black_1_18_even(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [2, 4, 6, 8, 10]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                expected = f'The spin resulted in {number} . . .\n' \
                           f'Pay {number}\n' \
                           f'Pay Black\n' \
                           f'Pay Even\n' \
                           f'Pay 1 to 18'
                result = mock_print.getvalue()
                self.assertIn(expected, result, '\nOutput different that the expected!')

    @patch('random.choice')
    def test_ok_black_19_36_odd(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [31, 33, 35]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'The spin resulted in {number} . . .\n'
                              f'Pay {number}\n'
                              'Pay Black\n'
                              'Pay Odd\n'
                              'Pay 19 to 36', result, 'Output different that the expected!')

    @patch('random.choice')
    def test_ok_black_19_36_even(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [20, 22, 24, 26, 28]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'The spin resulted in {number} . . .\n'
                              f'Pay {number}\n'
                              'Pay Black\n'
                              'Pay Even\n'
                              'Pay 19 to 36', result, 'Output different that the expected')

    # 00 and 0

    @patch('random.choice')
    def test_ok_00_0(self, mock_random):
        """
        Check if return the correct result
        """

        numbers = [00, 0]

        for number in numbers:
            mock_random.return_value = number

            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                sys.modules.pop(self.module_name, None)
                importlib.import_module(name=self.module_name, package='files')

                result = mock_print.getvalue()
                self.assertIn(f'Pay {number}', result, 'Output different that the expected')