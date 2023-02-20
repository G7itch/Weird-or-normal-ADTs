class Undefined:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return "Undefined({})".format(self.value)

    def __eq__(self, other):
        if isinstance(other, Undefined):
            return self.value == other.value
        return False

    def __bool__(self):
        return False
