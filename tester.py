from schedule import Schedule
from user import User
from course import Course
from event import Event
from event_time import EventTime
import time
import datetime


def test1():
    print("Test 1:")
    will = User("Will", Schedule())

    will.to_string()
    print()


def test2():
    print("Test 2:")
    reynaldo = User("Reynaldo", Schedule())

    reynaldo.schedule.add_course(Course("CSCI141", EventTime(("Mon"), 1000, 1200), "GOL"))

    reynaldo.to_string()
    print()


def test3():
    print("Test 3:")
    michael = User("Michael", Schedule())

    michael.schedule.add_course(Course("CSCI140", EventTime(("Mon", "Wed", "Fri"), 1200, 1400), "GOL"))

    print(michael.schedule.courses["CSCI140"].time.in_time(1300))  # True

    michael.schedule.add_event(Event("Skate", EventTime(("Mon"), 1800, 1900)))

    michael.to_string()


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
