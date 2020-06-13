class StreamChecker:

    def __init__(self, _streamChecker):
        self._streamChecker = _streamChecker

    def GetBroadcastStatus(self):
        return self._streamChecker.GetBroadcastStatus()

    def QuitProgram(self):
        return self._streamChecker.QuitProgram()