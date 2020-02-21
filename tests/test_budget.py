import unittest
import pprint

from machine_sleeping.budget import DailyEnergyBudget



class TestBudget(unittest.TestCase):
   def test_budget(self):
        deb = DailyEnergyBudget(20)
        deb.spend(10, 'foo')
        deb.spend(5, 'boo')
        deb.spend(15, 'doo')
        deb.replenish(50)

        print('\nDaily Budget History:')
        pprint.pprint(deb.history)

        assert deb.budget == 40


if __name__ == '__main__':
    unittest.main()
