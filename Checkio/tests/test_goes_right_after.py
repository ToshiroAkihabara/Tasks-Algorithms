import pytest

from Checkio.solution.goes_right_after import GoesAfter


@pytest.fixture
def sol() -> GoesAfter:
    """
    Initial GoesAfter
    """
    solution = GoesAfter()
    return solution


@pytest.mark.parametrize("word, first, second, result", [("cable", "a", "b", True)])
class TestGoesAfter:
    def test_goes_after(
        self, sol: GoesAfter, word: str, first: str, second: str, result: bool
    ) -> None:
        assert sol.goes_after(word, first, second) == result
