"""
Implement a rate limiter decorator that limits the number of times
a function can be called within a specific time window.
"""

import time
from collections import deque
from functools import wraps
from threading import Lock


class RateLimiter:
    def __init__(self, max_calls: int, time_window: float):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
        self.lock = Lock()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self.lock:
                now = time.time()

                # Remove old calls
                while self.calls and now - self.calls[0] >= self.time_window:
                    self.calls.popleft()

                # Check if we can make a new call
                if len(self.calls) >= self.max_calls:
                    raise Exception("Rate limit exceeded")

                self.calls.append(now)
                return func(*args, **kwargs)

        return wrapper


# Usage
@RateLimiter(max_calls=3, time_window=1.0)
def api_call(data):
    print(f"Processing {data}")
    return data


# Test
for i in range(5):
    try:
        api_call(f"request-{i}")
    except Exception as e:
        print(f"Request {i} failed: {e}")
