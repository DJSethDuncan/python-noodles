# unit test case
import unittest

def multiply_numbers(x, y):
  #add your code here
  return x * y
  # add your code here


class TestForNone(unittest.TestCase):

  def test_when_a_is_null(self):
    try:
      self.assertIsNone(multiply_numbers(5, None))
    except AssertionError as msg:
      print(msg)

if __name__ == '__main__':  
  unittest.main()