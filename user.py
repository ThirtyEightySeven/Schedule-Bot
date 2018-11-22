class User:
    __slots__ = ['name', 'schedule']

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def is_busy(self, time):
        for course in self.schedule.courses:
            if course.time.in_time(time):
                return True
        
        for event in self.schedule.events:
            if event.time.in_time(time):
                return True
        
        return False
        
    def is_conflict(self, start_one, end_one, start_two, end_two):
        return start_one < end_two and end_one > start_two


"""
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

"""