import unittest 
#from hello import *
from mumbler import *

class FirstTests(unittest.TestCase):

  def test_mumble_single_letters_lowercase(self):
    self.assertEqual(mumble_letters('a'),'A')
    
  def test_mumble_multiple_letters(self):
    self.assertEqual(mumble_letters('abC'),'A-Bb-Ccc')

  def test_mumble_multiple_letters_and_cases(self):
    self.assertEqual(mumble_letters('aBCd'),'A-Bb-Ccc-Dddd')

  def test_mumble_multiple_letters_and_cases(self):
    self.assertEqual(mumble_letters('QWERTY'),'Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy')

  def test_mumble_empty_edgecase(self):
    self.assertEqual(mumble_letters(''),'')

if __name__ == '__main__':
    unittest.main()