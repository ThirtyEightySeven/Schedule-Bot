class EventTime:
    __slots__ = "days", "start", "end"

    def __init__(self, days, start, end):
        self.days = days
        self.start = start
        self.end = end
    
    def parse_time(string_time):
        final_time = 0
        time_ampm = string_time.split()
    
        if ':' in time_ampm[0]:
            split_time = time_ampm[0].split(":")
            final_time += int(split_time[0]) * 100 + int(split_time[1])
        else:
            final_time += int(time_ampm[0]) * 100

        final_time += 1200 if time_ampm[1].lower() == "pm" else 0
        
        return final_time


    def in_time(self, current_time):
        return current_time >= self.start and current_time <= self.end

    def __repr__(self):
        return 'EventTime(days=%s, start=%s, end=%s)' % (self.days, self.start, self.end)