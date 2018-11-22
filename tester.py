from model.schedule import Schedule
from model.user import User
from model.course import Course
from model.event import Event
from model.event_time import EventTime
from model.data import Data
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


def test4():
    data = Data()
    data.add_user(123456, 'Will', User("Will", Schedule()))
    [print('%s: %s\n' % (k, v)) for k, v in data.db['users'].items()]
    print(data.db)
    # print(data.db['users']['Will'].schedule.events['Skate'].time.in_time(data.db['users']['Michael'].schedule.courses['CSCI140'].time.start))
    #print(data.db)
    data.write_data()
    #print(data.db)
    #data.read_data()
    #print(data.db)


def test5():
    print(EventTime.parse_time("2:00 AM"))
    print(EventTime.parse_time("2:40 PM"))
    print(EventTime.parse_time("4 AM"))

def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
