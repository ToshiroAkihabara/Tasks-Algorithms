class CountOcc:
    """pytest Checkio/tests/test_count_substring.py -v"""

    def count_occurrences(self, main: str, sub: str) -> int:
        main_str = main.lower()
        sub = sub.lower()
        targets = []
        for i in range(len(main)):
            if main_str.startswith(sub, i):
                targets.append(i)
        return len(targets)
