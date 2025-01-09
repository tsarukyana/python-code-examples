"""
Thread-safe Singleton pattern
"""
import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize only once
        if not hasattr(self, 'initialized'):
            with self._lock:
                if not hasattr(self, 'initialized'):
                    self.initialized = True
                    self.data = {}

    def set_data(self, key, value):
        with self._lock:
            self.data[key] = value

    def get_data(self, key):
        with self._lock:
            return self.data.get(key)


# Usage
instance1 = Singleton()
instance2 = Singleton()
print(instance1 is instance2)  # True
