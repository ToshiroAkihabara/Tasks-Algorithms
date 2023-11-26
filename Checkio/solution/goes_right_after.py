class GoesAfter:
    """pytest Checkio/tests/test_goes_right_after.py -v"""

    def goes_after(self, word: str, first: str, second: str) -> bool:
        return False if word.find(first + second) < 0 else True
