"""
This is a simple task scheduler that allows you to schedule tasks to run at a specific time in the future.
"""

import asyncio
import heapq
from datetime import datetime, timedelta
from typing import Callable, Awaitable, Any


class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self._counter = 0

    def schedule(self,
                 delay: timedelta,
                 coro: Callable[..., Awaitable[Any]],
                 *args,
                 **kwargs) -> int:
        self._counter += 1
        run_at = datetime.now() + delay
        heapq.heappush(self.tasks, (run_at, self._counter, coro, args, kwargs))
        return self._counter

    async def run(self):
        while self.tasks:
            run_at, counter, coro, args, kwargs = self.tasks[0]
            now = datetime.now()

            if now >= run_at:
                heapq.heappop(self.tasks)
                try:
                    await coro(*args, **kwargs)
                except Exception as e:
                    print(f"Task {counter} failed: {e}")
            else:
                await asyncio.sleep((run_at - now).total_seconds())


# Usage
async def print_message(msg: str):
    print(f"{datetime.now()}: {msg}")


async def main():
    scheduler = TaskScheduler()

    # Schedule some tasks
    scheduler.schedule(timedelta(seconds=2), print_message, "First task")
    scheduler.schedule(timedelta(seconds=1), print_message, "Second task")
    scheduler.schedule(timedelta(seconds=3), print_message, "Third task")

    await scheduler.run()


# Run the scheduler
asyncio.run(main())