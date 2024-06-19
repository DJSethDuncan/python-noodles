import unittest

def getGeneration(age):
    if age < 18:
        return 'zoomer'
    elif age < 40:
        return 'millenial'
    elif age < 60:
        return 'gen x'
    elif age < 80:
        return 'boomer'
    else:
        return 'senior'

class TestAssert(unittest.TestCase):
    def test_getGeneration(self):
      self.assertEqual(getGeneration(15), 'zoomer')
      self.assertEqual(getGeneration(25), 'millenial')
      self.assertNotEqual(getGeneration(25), 'gen x')

if __name__ == '__main__':
    unittest.main()