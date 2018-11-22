import datetime


class Event:
    __slots__ = "name", "time"

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return "**%s**\nTime:%s" % (self.name, self.time)

    def __repr__(self):
        return 'Event(%s, %s)' % (self.name, self.time) 
