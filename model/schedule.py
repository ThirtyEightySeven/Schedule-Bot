from model.course import Course
from model.event import Event


class Schedule:
    __slots__ = ['courses', 'events']

    def __init__(self, courses, events):
        self.courses = courses
        self.events = events

    def add_course(self, course):
        self.courses[course.code] = course

    def remove_course(self, course_name):
        del self.courses[course_name]
    
    def clear_courses(self):
        self.courses.clear()

    def add_event(self, event):
        self.events[event.name] = event

    def remove_event(self, event_name):
        del self.events[event_name]
    
    def clear_events(self):
        self.events.clear()
    
    def clear_schedule(self):
        self.clear_events()
        self.clear_courses()

    def __str__(self):
        return '\n' + ''.join([self.courses[course].__str__() + '\n' for course in self.courses]) + ''.join([self.events[event].__str__() + '\n' for event in self.events])

    def __repr__(self):
        return 'Schedule(%s, %s)' % (self.courses, self.events) 
