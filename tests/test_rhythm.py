import unittest
import pprint

from machine_sleeping.entity import CircamentRhythm



class TestCircamentRhythm(unittest.TestCase):
   def test_circadian_rhythm(self):
        rhythm = CircamentRhythm('sleep', 1)
        rhythm.setState('awake', 0.3)

        assert rhythm.certainty == 0.3


if __name__ == '__main__':
    unittest.main()
