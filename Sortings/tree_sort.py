import logging


class Treesort:
    def __init__(self, arr: list[int]) -> None:
        self.logger = logging.basicConfig(level=logging.DEBUG)
        self.arr = arr
        self.left = None
        self.right = None
        
    
        
