import logging
import random

import pytest
from Sort.e215_Kth_Largest_Element_in_an_Array import Solution


@pytest.fixture(autouse=True)
def quiet_logs():
    logging.disable(logging.CRITICAL)
    yield
    logging.disable(logging.NOTSET)


@pytest.fixture
def sol_inst():
    return Solution()


@pytest.mark.parametrize(
    "nums, k, res",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),                          # k = 1 — максимум
        ([2, 1], 2, 1),                          # k = n — минимум
        ([7, 7, 7, 7], 2, 7),                    # все элементы равны
        ([-1, -5, -3], 2, -3),                   # отрицательные
        ([1, 2, 3, 4, 5], 3, 3),                 # уже отсортирован
        ([5, 4, 3, 2, 1], 3, 3),                 # обратный порядок
        ([3, 3, 3, 1, 1], 2, 3),                 # k-й по порядку, а не k-й уникальный
    ]
)
def test_find_kth_largest(sol_inst, nums, k, res):
    assert sol_inst.findKthLargest(list(nums), k) == res


@pytest.mark.parametrize("size", [1, 2, 17, 64, 300])
def test_all_k_match_sorted(sol_inst, size):
    # перебираем ВСЕ k от 1 до n и сверяем с отсортированным массивом
    random.seed(size)
    nums = [random.randint(-30, 30) for _ in range(size)]   # с дубликатами
    expected = sorted(nums, reverse=True)

    for k in range(1, size + 1):
        assert sol_inst.findKthLargest(list(nums), k) == expected[k - 1], f"k={k}"


@pytest.mark.parametrize(
    "name, nums",
    [
        ("уже отсортирован", list(range(5000))),
        ("обратный порядок", list(range(5000, 0, -1))),
        ("все элементы равны", [42] * 5000),
    ]
)
def test_worst_cases(sol_inst, name, nums):
    # схема Ломуто на массиве из одинаковых элементов деградирует до O(n^2)
    # (об этом комментарий в самом решении); схема Хоара должна выдерживать
    k = len(nums) // 2
    assert sol_inst.findKthLargest(list(nums), k) == sorted(nums, reverse=True)[k - 1], name
