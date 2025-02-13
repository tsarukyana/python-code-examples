"""
Circular buffer is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end.
"""

from threading import Lock
from collections import deque
from typing import TypeVar, Generic

T = TypeVar('T')


class CircularBuffer(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.buffer = deque(maxlen=size)
        self.lock = Lock()

    def push(self, item: T) -> bool:
        with self.lock:
            if len(self.buffer) == self.size:
                self.buffer.popleft()
            self.buffer.append(item)
            return True

    def pop(self) -> T:
        with self.lock:
            if not self.buffer:
                raise IndexError("Buffer is empty")
            return self.buffer.popleft()

    def peek(self) -> T:
        with self.lock:
            if not self.buffer:
                raise IndexError("Buffer is empty")
            return self.buffer[0]

    def __len__(self) -> int:
        with self.lock:
            return len(self.buffer)


# Usage
buffer = CircularBuffer[int](3)
buffer.push(1)
buffer.push(2)
buffer.push(3)
buffer.push(4)  # Overwrites 1
print(list(buffer.buffer))  # [2, 3, 4]
