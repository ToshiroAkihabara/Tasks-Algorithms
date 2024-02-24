import logging
from collections import deque
from queue import LifoQueue


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)


class QueueLIFO(Logger):
    """
    You should to use LifoQueue in threading projects.
    """

    def __init__(self) -> None:
        super(QueueLIFO, self).__init__()
        self.stack = LifoQueue()

    def put(self, item: int) -> None:
        self.stack.put(item)
        logging.debug(f"Inserted a {item} into the stack")

    def get(self) -> int:
        if not self.stack.empty():
            item = self.stack.get()
            logging.debug(f"Got an elements {item} from the stack")
            return item
        logging.debug("Stack is empty")

    def __str__(self):
        return self.stack


class DequeLIFO(Logger):
    """
    You should to use deque for non-threading projects.
    """

    def __init__(self) -> None:
        super(DequeLIFO, self).__init__()
        self.stack = deque([])

    def append(self, item: int) -> None:
        self.stack.append(item)
        logging.debug(f"Inserted a {item} into the stack")

    def pop(self) -> int:
        if not self.empty():
            item = self.stack.pop()
            logging.debug(f"Got an elements {item} from the stack")
            return item
        logging.debug("Stack is empty")

    def empty(self) -> bool:
        return len(self.stack) == 0

    def __str__(self):
        return self.stack
