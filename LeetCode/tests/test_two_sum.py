import pytest

from LeetCode.two_sum.two_sum_solution import TwoSumSolution


@pytest.fixture()
def sol() -> TwoSumSolution:
    solution = TwoSumSolution()
    return solution


@pytest.mark.parametrize(
    "test_nums, test_target, expected_result",
    [
        ([2, 1, 7, 8, 10, 3, 2, 5, 4, 9], 5, [0, 5]),
    ],
)
class TestSolution:
    def test_two_sum_first(
        self, sol: TwoSumSolution, test_nums: list, test_target: int, expected_result: list
    ) -> None:
        assert sol.two_sum_first(test_nums, test_target) == expected_result

    def test_two_sum_second(
        self, sol: TwoSumSolution, test_nums: list, test_target: int, expected_result: list
    ) -> None:
        assert sol.two_sum_second(test_nums, test_target) == expected_result

    def test_two_sum_third(
        self, sol: TwoSumSolution, test_nums: list, test_target: int, expected_result: list
    ) -> None:
        assert sol.two_sum_third(test_nums, test_target) == expected_result

    def test_two_sum_four(self, sol: TwoSumSolution, test_nums: list, test_target: int, expected_result: list) -> None:
        assert sol.two_sum_four(test_nums, test_target) == expected_result
