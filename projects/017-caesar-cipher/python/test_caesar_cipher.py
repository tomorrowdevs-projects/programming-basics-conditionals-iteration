import importlib
import io
import os
import sys
from pathlib import Path
from unittest import TestCase, skipIf
from unittest.mock import patch

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0


@skipIf(is_file_empty, 'Empty file. Test 017 Skipped')
class TestCaesarCipher(TestCase):

    def setUp(self) -> None:
        self.module_name = 'projects.017-caesar-cipher.python.main'

    @patch('builtins.input')
    def test_encode_ok(self, mock_inputs):
        """
        Check if return the correct result
        """

        mock_inputs.side_effect = ['whispering leaves in the moonlight', 2]

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue()
            ok_result = 'yjkurgtkpi ngcxgu kp vjg oqqpnkijv'

            result = [x.lower() for x in result.split('\n')][0]
            self.assertEqual(ok_result, result, 'Output different that the expected')

    @patch('builtins.input')
    def test_decode_ok(self, mock_inputs):
        """
        Check if return the correct result
        """

        mock_inputs.side_effect = ['yjkurgtkpi ngcxgu kp vjg oqqpnkijv', -2]

        with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
            sys.modules.pop(self.module_name, None)
            importlib.import_module(name=self.module_name, package='files')

            result = mock_print.getvalue()
            ok_result = 'whispering leaves in the moonlight'

            result = [x.lower() for x in result.split('\n')][0]
            self.assertEqual(ok_result, result, 'Output different that the expected')