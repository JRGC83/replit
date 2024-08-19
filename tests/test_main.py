import sys
import os
import unittest

# Adjust the Python path to include the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import your function from the main module
from main import your_function  # Replace 'main' and 'your_function' with your actual module and function names



class TestMain(unittest.TestCase):

  def setUp(self):
    self.value = 10
  
  def test_function(self):
    result = your_function(self.value)
    self.assertEqual(result, None)
    
  
  def tearDown(self):
    self.value = None

if __name__ == '__main__':
  unittest.main()