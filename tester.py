from schedule import Schedule
from user import User
from course import Course
from event_time import EventTime
import time
import datetime

def main():
    miguel = User('Miguel', Schedule())
    print(time.asctime(time.localtime(time.time())))
    miguel.schedule.add_course(Course("CSCI140", EventTime(("Mon", "Wed", "Fri"), 1200, 1400), "GOL"))
    print(miguel.schedule.courses)
    print(miguel.schedule.courses["CSCI140"].time.in_time(1100))


if __name__ == "__main__":
    main()                                                                