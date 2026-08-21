import random

import pytest
from Sort.hoar_scheme_partition import hoare_partition
from Sort.lomuto_scheme_devision import lomuto_partition


def random_array(seed, size, spread=15):
    random.seed(seed)
    return [random.randint(-spread, spread) for _ in range(size)]


# --- схема Хоара -----------------------------------------------------------

@pytest.mark.parametrize("seed", range(20))
def test_hoare_splits_into_two_zones(seed):
    nums = random_array(seed, random.Random(seed).randint(2, 30))
    original = list(nums)

    j = hoare_partition(nums, 0, len(nums) - 1)

    assert sorted(nums) == sorted(original), "состав массива изменился"
    assert 0 <= j <= len(nums) - 1
    # Хоар не ставит пивот на место, а лишь проводит границу:
    # всё слева от неё <= всего, что справа
    if j < len(nums) - 1:
        assert max(nums[:j + 1]) <= min(nums[j + 1:])


@pytest.mark.parametrize(
    "nums, left, right",
    [
        ([2, 1], 0, 1),
        ([1, 1, 1, 1], 0, 3),
        ([5, 5, 3, 5], 0, 3),
        ([-3, 0, -3, 7, 7], 0, 4),
    ]
)
def test_hoare_on_duplicates(nums, left, right):
    original = list(nums)
    j = hoare_partition(nums, left, right)

    assert sorted(nums) == sorted(original)
    assert left <= j <= right
    if j < right:
        assert max(nums[left:j + 1]) <= min(nums[j + 1:right + 1])


def test_hoare_boundary_can_reach_right(monkeypatch):
    """Граница j == right возможна, если пивотом случайно выбран строгий
    максимум, стоящий последним: тогда левый указатель проходит весь
    диапазон. Подмассив при этом не уменьшается — вызывающий код должен
    это переживать (в 215 следующий вызов берёт новый случайный пивот).
    См. раздел «Частые ошибки» в README."""
    nums = [1, 2]
    monkeypatch.setattr(random, "randint", lambda a, b: b)   # пивот = nums[right]

    assert hoare_partition(nums, 0, 1) == 1                  # == right


def test_hoare_boundary_shrinks_with_inner_pivot(monkeypatch):
    """Если пивот брать из [left, right - 1], j == right невозможен —
    это классическая гарантия схемы Хоара."""
    for seed in range(50):
        nums = random_array(seed, random.Random(seed).randint(2, 20))
        right = len(nums) - 1
        monkeypatch.setattr(random, "randint", lambda a, b, _r=right: min(a, _r - 1))

        assert hoare_partition(nums, 0, right) < right


# --- схема Ломуто ----------------------------------------------------------

@pytest.mark.parametrize("seed", range(20))
def test_lomuto_places_pivot_exactly(seed):
    nums = random_array(seed, random.Random(seed).randint(1, 30))
    original = list(nums)

    p = lomuto_partition(nums, 0, len(nums) - 1)

    assert sorted(nums) == sorted(original), "состав массива изменился"
    assert 0 <= p <= len(nums) - 1
    # Ломуто, в отличие от Хоара, ставит пивот на его ОКОНЧАТЕЛЬНОЕ место
    assert all(x < nums[p] for x in nums[:p])
    assert all(x >= nums[p] for x in nums[p + 1:])


@pytest.mark.parametrize(
    "nums",
    [
        [1],
        [2, 1],
        [1, 1, 1, 1],
        [5, 5, 3, 5],
        [-3, 0, -3, 7, 7],
    ]
)
def test_lomuto_on_duplicates(nums):
    original = list(nums)
    p = lomuto_partition(nums, 0, len(nums) - 1)

    assert sorted(nums) == sorted(original)
    assert all(x < nums[p] for x in nums[:p])
    assert all(x >= nums[p] for x in nums[p + 1:])


def test_lomuto_all_equal_gives_worst_split(monkeypatch):
    """Почему Ломуто ловит TLE на 215: если все элементы равны, условие
    `nums[i] < pivot` не выполняется никогда, store_idx остаётся на left,
    и разбиение получается 0 / n-1 — то есть O(n^2) вместо O(n)."""
    nums = [7] * 10
    assert lomuto_partition(nums, 0, 9) == 0
