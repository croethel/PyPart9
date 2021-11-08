import unittest

from PyPart9.json_helper import read_json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = """{'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang',
         'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}"""
        actual = read_json('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/link.json')
        self.assertEqual(expected, actual)# add assertion here

#create simple json file that has limited info in it, simplifies =




if __name__ == '__main__':
    unittest.main()
