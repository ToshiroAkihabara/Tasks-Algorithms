import pytest

from Checkio.solution.count_substring import CountOcc


@pytest.fixture
def sol() -> CountOcc:
    """
    Initial CountOcc
    """
    solution = CountOcc()
    return solution


@pytest.mark.parametrize("main, target, result", [("Hello world hello", "hello", 2)])
class TestCountOcc:
    def test_count_occurrences(
        self, sol: CountOcc, main: str, target: str, result: int
    ) -> None:
        assert sol.count_occurrences(main, target) == result
