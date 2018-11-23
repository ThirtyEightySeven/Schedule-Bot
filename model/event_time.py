from model.constants import day_dict
import datetime

class EventTime:
    __slots__ = ['days', 'start', 'end']

    def __init__(self, days=set(), start=0, end=0):
        self.days = days
        self.start = start
        self.end = end
    
    def parse_input(self, input_str) -> None:
        if input_str is None:
            return 

        while not input_str[0].isdigit():
            self.days.add(day_dict[input_str[0]])
            input_str = input_str[1:]
        
        start_str = ''
        while len(input_str) > 0 and (input_str[0].isdigit() or input_str[0] == ':'):
            start_str += input_str[0]
            input_str = input_str[1:]
        
        start_str += ' '

        while len(input_str) > 0 and not input_str[0].isdigit():
            start_str += input_str[0]
            input_str = input_str[1:]
        
        self.start = self.parse_time(start_str)

        end_str = ''
        while len(input_str) > 0 and (input_str[0].isdigit() or input_str[0] == ':'):
            end_str += input_str[0]
            input_str = input_str[1:]
        
        end_str += ' '

        while len(input_str) > 0 and not input_str[0].isdigit():
            end_str += input_str[0]
            input_str = input_str[1:]
        
        self.end = self.parse_time(end_str)

        print(self.start, self.end)
        
    def parse_time(self, string_time: str) -> int:
        final_time = 0
        time_ampm = string_time.split()
    
        if ':' in time_ampm[0]:
            split_time = time_ampm[0].split(":")
            if int(split_time[0]) == 12:
                split_time[0] = '00'
            final_time += int(split_time[0]) * 100 + int(split_time[1])
        else:
            final_time += int(time_ampm[0]) * 100

        if time_ampm[1].lower()[0] == 'p' and not (1200 <= final_time <= 1259):
            final_time += 1200
        
        return (final_time, time_ampm[1])

    def format_time(self, basic_time):
        new_basic_time = basic_time[0]

        if basic_time[0] > 1159:
            new_basic_time -= 1200
        
        str_time = str(datetime.time(new_basic_time // 100, new_basic_time % 100))
    
        if new_basic_time < 1000:
            str_time = str_time[1:]

        if basic_time[0] >= 1200 and new_basic_time >= 100:
            str_time = str_time[:-3] + " PM"
        elif new_basic_time < 100:
            print("YEET")
            str_time = "12" + str_time[1:-3]
            if basic_time[1] == 'A':
                str_time += " AM"
            elif basic_time[1] == 'P':
                str_time += " PM"
            else:
                raise Exception("Invalid time format.")
        else:
            str_time = str_time[:-3] + " AM"

        return str_time

    def in_time(self, current_time: int) -> bool:
        return current_time >= self.start and current_time <= self.end

    def __str__(self) -> str:
        return 'Day(s): %s\nStart: %s\nEnd: %s' % (sorted(self.days, key=["Mon", "Tue", "Wed", "Thu", "Fri"].index), self.format_time(self.start), self.format_time(self.end))

    def __repr__(self) -> str:
        return 'EventTime(days=%s, start=%s, end=%s)' % (sorted(self.days, key=["Mon", "Tue", "Wed", "Thu", "Fri"].index), self.format_time(self.start), self.format_time(self.end))