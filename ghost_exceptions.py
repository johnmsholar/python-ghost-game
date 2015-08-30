# Defining a series of exceptions to capture when players want to conduct moves that are not letter moves

class CallBluffException(Exception):
    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return repr(self.value)

class HelpException(Exception):
    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return repr(self.value)

class EndRoundException(Exception):
    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return repr(self.value)

class OpponentCompletedWordException(Exception):
    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return repr(self.value)