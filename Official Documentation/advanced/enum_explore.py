from enum import Enum, auto

class Office:
    def __init__(self, weekday):
        self._weekday = weekday

    @property
    def office_weekday(self):
        return self._weekday

    def __repr__(self):
        return f"< {self._weekday} >"

class Day(Enum):
    Saturday = auto()
    Friday = auto()
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thurseday = auto()
    Sunday = auto()

def enumeration_test():
    print(Day.Saturday)
    print(Day.Friday)

    o = Office(Day.Friday)

    # following is used as property
    print(o.office_weekday)
    print(o)

enumeration_test()

