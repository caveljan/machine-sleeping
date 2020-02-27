import unittest
import pprint

from machine_sleeping.entity import CircamentRhythm



class TestCircamentRhythm(unittest.TestCase):
   def test_circament_rhythm(self):
        rhythm = CircamentRhythm('sleep', 1, 1)
        rhythm.setState('awake', 1, 0.3)

        assert rhythm.state_certainty == 0.3


if __name__ == '__main__':
    unittest.main()
