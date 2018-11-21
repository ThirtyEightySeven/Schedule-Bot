class User:
    __slots__ = ['name', 'schedule']
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
