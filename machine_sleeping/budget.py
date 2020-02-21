import time



class DailyEnergyBudget:
    def __init__(self, value: int):
        self.budget = value
        self.history = []

    def spend(self, value: int, action: str):
        self.budget = self.budget - value
        spent = {
            "timestamp": time.time(),
            "value": value,
            "action": action,
            "budget_after": self.budget,
        }
        self.history.append(spent)

    def replenish(self, value: int):
        self.budget = self.budget + value
