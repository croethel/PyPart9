from unittest import TestCase
from json_helper import read_json, read_all_json_files, write_pickle, load_pickle
import json
import os
import pickle
import io import StringIO
from unittest.mock import patch



class TestJasonHelper(TestCase):

    # Part A
    def test_read_json(self):
        expected = {'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang', 'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}
        actual = read_json('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/link.json')
        err = f'Expected: {expected} | Actual: {actual}'
        self.assertEqual(expected, actual, err)


    # Part B
    def test_read_all_json(self):
        expected = [
            {'name': 'Mario', 'neutral_special': 'Fireball', 'side_special': 'Cape', 'up_special': 'Super Jump Punch',
              'down_special': 'F.L.U.D.D.', 'final_smash': 'Mario Finale'},
             {'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang',
              'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}
        ]
        actual = read_all_json_files('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/')
        err = f'Expected: {expected} | Actual: {actual}'
        self.assertEqual(expected, actual, err)


    # Part C
 #   def test_write_pickle(self):
 #       expected =
 #       actual =
 #       self.assertEqual(expected, actual)


    # Part D
 #   def test_load_pickle(self):
 #       expected =
 #       actual =
 #       self.assertEqual(expected, actual)


