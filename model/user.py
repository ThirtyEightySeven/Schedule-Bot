class User:
    __slots__ = ['name', 'schedule']

    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def is_busy(self, time):
        for course in self.schedule.courses:
            if self.schedule.courses[course].time.in_time(time):
                return True

        for event in self.schedule.events:
            if self.schedule.events[event].time.in_time(time):
                return True

        return False

    def is_conflict(self, start_one, end_one, start_two, end_two):
        return start_one < end_two and end_one > start_two

    def __str__(self):
        return '**Name**: %s\n__**Schedule**__: %s' % (self.name, self.schedule)

    def __repr__(self):
        return 'User(%s, %s)' % (self.name, self.schedule)
