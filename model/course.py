import datetime


class Course:
    __slots__ = ['code', 'time', 'location']

    def __init__(self, code, time, location):
        self.code = code
        self.time = time
        self.location = location

    def __str__(self):
        return "**%s**: \n%s\nLocation: %s" % (self.code, self.time, self.location)

    def __repr__(self):
        return 'Course(%s, %s, %s)' % (self.code, self.time, self.location) 