import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 016 Skipped')
class TestFizzBuzz(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.016-fizz-buzz.python.main'

    def test_ok(self):
        """
        Check if return the correct result
        """

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue()
            ok_result = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14',
                         'fizz buzz', '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23', 'fizz', 'buzz', '26',
                         'fizz', '28', '29', 'fizz buzz', '31', '32', 'fizz', '34', 'buzz', 'fizz', '37', '38', 'fizz',
                         'buzz', '41', 'fizz', '43', '44', 'fizz buzz', '46', '47', 'fizz', '49', 'buzz', 'fizz', '52',
                         '53', 'fizz', 'buzz', '56', 'fizz', '58', '59', 'fizz buzz', '61', '62', 'fizz', '64', 'buzz',
                         'fizz', '67', '68', 'fizz', 'buzz', '71', 'fizz', '73', '74', 'fizz buzz', '76', '77', 'fizz',
                         '79', 'buzz', 'fizz', '82', '83', 'fizz', 'buzz', '86', 'fizz', '88', '89', 'fizz buzz', '91',
                         '92', 'fizz', '94', 'buzz', 'fizz', '97', '98', 'fizz', 'buzz', '']

            result = [x.lower() for x in result.split('\n')]
            self.assertEqual(ok_result, result, 'Output different that the expected')
