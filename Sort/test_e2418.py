import random

import pytest
from Sort.e2418_Sort_the_People import Solution


@pytest.fixture
def sol_inst():
    return Solution()


@pytest.mark.parametrize(
    "method_name",
    ["sortPeople", "selectionSort", "myFirstSolution"]
)
@pytest.mark.parametrize(
    "names, heights, res",
    [
        (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
        (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
        (["Solo"], [42], ["Solo"]),
        (["A", "B"], [1, 2], ["B", "A"]),                    # обратный порядок
        (["A", "B"], [2, 1], ["A", "B"]),                    # уже отсортирован
        (["A", "B", "C", "D"], [10, 40, 20, 30], ["B", "D", "C", "A"]),
    ]
)
def test_sort_people(sol_inst, method_name, names, heights, res):
    assert getattr(sol_inst, method_name)(names, heights) == res


@pytest.mark.parametrize("method_name", ["selectionSort", "myFirstSolution"])
def test_input_not_mutated(sol_inst, method_name):
    # решение не должно портить переданные списки
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]

    getattr(sol_inst, method_name)(names, heights)

    assert names == ["Mary", "John", "Emma"]
    assert heights == [180, 165, 170]


@pytest.mark.parametrize("size", [1, 2, 17, 50])
def test_selection_matches_builtin(sol_inst, size):
    # рост по условию уникален — генерируем перестановку без повторов
    random.seed(size)
    heights = random.sample(range(1, 10 ** 5), size)
    names = [f"p{i}" for i in range(size)]

    expected = [n for _, n in sorted(zip(heights, names), reverse=True)]
    assert sol_inst.selectionSort(names, heights) == expected
    assert sol_inst.myFirstSolution(names, heights) == expected
