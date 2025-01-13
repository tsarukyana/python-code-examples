"""
This is a simple event system using descriptors. It allows you to define events in your classes and subscribe to them.
"""

from typing import Set, Callable
from weakref import WeakKeyDictionary


class Event:
    def __init__(self):
        self.handlers: WeakKeyDictionary[object, Set[Callable]] = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance not in self.handlers:
            self.handlers[instance] = set()
        return EventHandle(self, instance)


class EventHandle:
    def __init__(self, event: Event, instance: object):
        self.event = event
        self.instance = instance

    def subscribe(self, handler: Callable):
        self.event.handlers[self.instance].add(handler)

    def unsubscribe(self, handler: Callable):
        self.event.handlers[self.instance].remove(handler)

    def __call__(self, *args, **kwargs):
        for handler in self.event.handlers[self.instance]:
            handler(*args, **kwargs)


class Button:
    clicked = Event()
    value_changed = Event()

    def __init__(self, label: str):
        self.label = label
        self._value = 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int):
        old_value = self._value
        self._value = new_value
        if old_value != new_value:
            self.value_changed(old_value, new_value)

    def click(self):
        self.clicked(self.label)


# Usage
def on_click(label):
    print(f"Button {label} clicked!")


def on_value_change(old_value, new_value):
    print(f"Value changed from {old_value} to {new_value}")


button = Button("Test")
button.clicked.subscribe(on_click)
button.value_changed.subscribe(on_value_change)

button.click()  # Prints: Button Test clicked!
button.value = 42  # Prints: Value changed from 0 to 42
