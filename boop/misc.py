class Token(object):
    def __init__(self):
        self.type = ""
        self.value = ""
        self.line = 0
        self.num = 0
        self.isString = False

    def setType(self, type):
        self.type = type

    def setValue(self, value):
        self.value = value

    def setLine(self, line):
        self.line = line

    def setString(self, bool):
        self.isString = bool

    def setNum(self, num):
        self.num = num


class Program(object):
    def __init__(self):
        self.variables = {}
        self.events = []
        self.functions = {}

    def terminate(self):
        self = None
        print("[Program Terminated]")
        exit(2)

    def kill(self):
        self = None
        print("[Program Killed]")
        exit(1)


class BoopError(Exception):
    pass


token_types = {
    "PRINT": r"(print)",
    "INPUT": r"(input)",
    "PLUS": r"(\+)",
    "MINUS": r"(-)",
    "TIMES": r"(\*)",
    "DIVIDE": r"(\\)",
    "EQUALS": r"(=)",
    "INT": r"(\d+)",
    "ID": r":([a-zA-z]+)?",
    "STRING": r"([^\n]+)"
}
