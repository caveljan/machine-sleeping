class Sleep:
    def NREM(self):
        print('NREM')

    def REM(self):
        print('REM')


class Awake:
    def act(self):
        print('act')


class Entity:
    def __init__(self, state):
        self.state = state

    def sleep(self):
        self.state = 'sleep'

    def awake(self):
        self.state = 'awake'

    def getState(self):
        return self.state
