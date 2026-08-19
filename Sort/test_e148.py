import random

import pytest
from Sort.e148_Sort_List import Solution, ListNode, makeList


def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.fixture
def sol_inst():
    return Solution()


@pytest.mark.parametrize(
    "list_vals, res_vals",
    [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),      # обратный порядок
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),      # уже отсортирован
        ([3, 1, 3, 1, 2], [1, 1, 2, 3, 3]),      # дубликаты
        ([7, 7, 7], [7, 7, 7]),                  # все элементы равны
        ([-5, -1, -3], [-5, -3, -1]),            # только отрицательные
    ]
)
def test_sort_list(sol_inst, list_vals, res_vals):
    result = sol_inst.sortList(makeList(list_vals))
    assert to_array(result) == res_vals


@pytest.mark.parametrize("size", [16, 63, 100])
def test_sort_list_random(sol_inst, size):
    random.seed(size)
    vals = [random.randint(-100, 100) for _ in range(size)]
    result = sol_inst.sortList(makeList(vals))
    assert to_array(result) == sorted(vals)


def test_divide_splits_in_half(sol_inst):
    # divide отрезает первую половину: для чётной длины пополам,
    # для нечётной левая часть на один элемент длиннее
    left, right = sol_inst.divide(makeList([1, 2, 3, 4]))
    assert to_array(left) == [1, 2]
    assert to_array(right) == [3, 4]

    left, right = sol_inst.divide(makeList([1, 2, 3, 4, 5]))
    assert to_array(left) == [1, 2, 3]
    assert to_array(right) == [4, 5]


def test_merge_two_sorted_lists(sol_inst):
    result = sol_inst.merge(makeList([1, 3, 5]), makeList([2, 4, 6]))
    assert to_array(result) == [1, 2, 3, 4, 5, 6]

    # один из списков пуст
    assert to_array(sol_inst.merge(makeList([1, 2]), None)) == [1, 2]
    assert to_array(sol_inst.merge(None, makeList([1, 2]))) == [1, 2]
    assert sol_inst.merge(None, None) is None


def test_no_cycle_in_result(sol_inst):
    # перецепка указателей — частый источник зацикливания списка
    head = sol_inst.sortList(makeList([4, 2, 1, 3, 5]))
    seen = set()
    while head:
        assert id(head) not in seen, "в результате образовался цикл"
        seen.add(id(head))
        head = head.next
