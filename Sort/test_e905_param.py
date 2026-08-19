import pytest
from Sort.e905_Sort_Array_By_Parity import Solution

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "nums",
    [
        [3, 1, 2, 4],
        [0],
        [1, 3, 5],
        [2, 4, 6],
        [],
        [5, 2, 4, 1, 3, 0],
    ]
)
def test_sort(sol_inst, nums):
    # LeetCode принимает ЛЮБОЙ порядок внутри групп, поэтому проверяем свойство,
    # а не конкретный массив: сначала все чётные, потом все нечётные, состав тот же.
    result = sol_inst.sortArrayByParity(list(nums))

    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]

    assert result == evens + odds          # все чётные впереди всех нечётных
    assert sorted(result) == sorted(nums)  # состав массива не изменился
