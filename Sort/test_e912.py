import logging
import random

import pytest
from Sort.e912_Bubble_Sort_an_Array import Solution, bubble_sort, heap_sort


@pytest.fixture(autouse=True)
def quiet_logs():
    # решение логирует весь массив на каждый вызов — в тестах это лишний шум
    logging.disable(logging.CRITICAL)
    yield
    logging.disable(logging.NOTSET)


@pytest.fixture
def sol_inst():
    return Solution()


CASES = [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),            # уже отсортирован
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),            # обратный порядок
    ([7, 7, 7, 7], [7, 7, 7, 7]),                  # все элементы равны
    ([-5, 3, -1, 0, -5], [-5, -5, -1, 0, 3]),      # отрицательные и дубликаты
]


@pytest.mark.parametrize("nums, result", CASES)
def test_sort_array_quick_sort(sol_inst, nums, result):
    assert sol_inst.sortArray(list(nums)) == result


@pytest.mark.parametrize("nums, result", CASES)
def test_bubble_sort(nums, result):
    assert bubble_sort(list(nums)) == result


@pytest.mark.parametrize("nums, result", CASES)
def test_heap_sort(nums, result):
    assert heap_sort(list(nums)) == result


@pytest.mark.parametrize("size", [17, 64, 500])
def test_quick_sort_matches_builtin(sol_inst, size):
    random.seed(size)
    nums = [random.randint(-50, 50) for _ in range(size)]   # много дубликатов
    assert sol_inst.sortArray(list(nums)) == sorted(nums)


@pytest.mark.parametrize(
    "name, nums",
    [
        ("уже отсортирован", list(range(2000))),
        ("обратный порядок", list(range(2000, 0, -1))),
        ("все элементы равны", [42] * 2000),
        ("две различных величины", [0, 1] * 1000),
    ]
)
def test_quick_sort_worst_cases(sol_inst, name, nums):
    # именно на этих входах quick sort с пивотом-краем деградирует до O(n^2)
    # и уходит в RecursionError; случайный пивот должен их выдерживать
    assert sol_inst.sortArray(list(nums)) == sorted(nums), name


def test_quick_sort_is_in_place(sol_inst):
    # sortArray сортирует переданный список на месте и возвращает его же
    nums = [3, 1, 2]
    result = sol_inst.sortArray(nums)
    assert result is nums
    assert nums == [1, 2, 3]
