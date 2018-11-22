from model.course import Course
from model.event import Event


class Schedule:
    __slots__ = ['courses', 'events']

    def __init__(self, courses={}, events={}):
        self.courses = courses
        self.events = events

    def add_course(self, course):
        self.courses[course.code] = course

    def remove_course(self, course):
        del self.courses[course.code]
    
    def add_event(self, event):
        self.events[event.name] = event

    def remove_event(self, event):
        del self.events[event.name]

    def __str__(self):
        return '\n' + ''.join([self.courses[course].__str__() + '\n' for course in self.courses]) + ''.join([self.events[event].__str__() + '\n' for event in self.events])

    def __repr__(self):
        return 'Schedule(%s, %s)' % (self.courses, self.events) 
