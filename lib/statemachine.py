import time


class State(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value


class StateMachine(object):

    def __init__(self):
        self.currentState = None
        self.states = {}
        self.startTime = time.time()
        self.firstTimeInState = False

        # has to be run every cycle
    def STATEMACHINE(self):
        if not self.firstTimeInState:
            self.firstTimeInState = False

    def cur_state(self):
        return self.currentState

    def add_state(self, state):
        self.states[state.name] = state

    def add_states(self, states):
        for state in states:
            self.states[state.name] = state

    def go_to_state(self, newState):
        self.currentState = self.states[newState.name]
        self.startTime = time.time()
        self.firstTimeInState = True

    def elapsed_time(self):
        return time.time() - self.startTime

    @property
    def first_time(self) -> bool:
        return self.firstTimeInState
