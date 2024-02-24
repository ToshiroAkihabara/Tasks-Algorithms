import pytest

from Checkio.solution.replace_all_occ import ReplaceWord


@pytest.fixture
def sol() -> ReplaceWord:
    """
    Initial ReplaceWord
    """
    solution = ReplaceWord()
    return solution


@pytest.mark.parametrize(
    "main, target, repl, result",
    [("hello world", "world", "TypeScript", "hello TypeScript")],
)
class TestReplaceWord:
    def test_replace_word(
        self, sol: ReplaceWord, main: str, target: str, repl: str, result: str
    ) -> None:
        assert sol.replace_word(main, target, repl) == result
