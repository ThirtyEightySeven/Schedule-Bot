class EventTime:
    __slots__ = "days", "start", "end"

    def __init__(self, days, start, end):
        self.days = days
        self.start = start
        self.end = end

    def in_time(self, current_time):
        if current_time >= self.start and current_time <= self.end:
            return True
        return False
