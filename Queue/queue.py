import logging
from collections import deque


class FIFO:
    def __init__(self) -> None:
        logging.basicConfig(level=logging.DEBUG)
        self.queue = deque([])

    def append(self, item: int) -> None:
        self.queue.append(item)
        logging.debug(f"Inserted a {item} into the queue")

    def pop(self) -> int | None:
        if not self.empty():
            item = self.queue.popleft()
            logging.debug(f"Got an element {item} from the queue")
            return item
        logging.debug("Queue is empty")

    def empty(self) -> bool:
        return len(self.queue) == 0

    def __str__(self):
        return self.queue
