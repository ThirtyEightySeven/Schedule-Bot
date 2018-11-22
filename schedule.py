from _class import Class
from event import Event

class Schedule:
    __slots__ = ['classes', 'events']
    def __init__(self, classes={}, events={}):
        self.classes = classes
        self.events = events
    
    def add_class(self, _class):
        self.classes[_class.name] = _class
    
    def remove_class(self, _class):
        del self.classes[_class.name]                

    def add_event(self, event):
        self.events[event.name] = event

    def remove_event(self, event):
        del self.events[event.name] 