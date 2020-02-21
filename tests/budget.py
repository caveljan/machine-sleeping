from machine_sleeping.budget import DailyEnergyBudget



def test_budget():
    deb = DailyEnergyBudget(20)
    deb.spend(10, 'foo')
    deb.spend(5, 'boo')
    deb.spend(15, 'doo')
    deb.replenish(50)
    assert deb.budget == 40


if __name__ == '__main__':
    test_budget()
    print("Everything passed")
