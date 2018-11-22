class EventTime:
    __slots__ = "days", "start", "end"

    def __init__(self, days, start, end):
        self.days = days
        self.start = start
        self.end = end

    def in_time(self, current_time):
        return current_time >= self.start and current_time <= self.end

    def __repr__(self):
        return 'EventTime(days=%i, start=%i, end=%i)' % (self.days, self.start, self.end)