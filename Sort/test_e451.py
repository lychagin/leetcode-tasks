import pytest
from Sort.e451_Sort_Characters_By_Frequency_Bucket_sort import Solution

@pytest.fixture
def sol_inst():
    return Solution()


def is_valid(result: str, s: str) -> bool:
    """Ответ верен, если состав символов совпал, одинаковые символы стоят
    подряд, а частоты идут по невозрастанию. Конкретный порядок символов
    с равной частотой условием задачи не зафиксирован."""
    if sorted(result) != sorted(s):
        return False

    groups = []
    for ch in result:
        if groups and groups[-1][0] == ch:
            groups[-1][1] += 1
        else:
            groups.append([ch, 1])

    chars = [ch for ch, _ in groups]
    if len(chars) != len(set(chars)):       # символ разбит на несколько групп
        return False

    counts = [cnt for _, cnt in groups]
    return counts == sorted(counts, reverse=True)


@pytest.mark.parametrize(
    "method_name",
    ["BucketSort", "TimSort"]
)
@pytest.mark.parametrize(
    "s",
    ["tree", "cccaaa", "Aabb", "a", "abcdef", "eeeeddd cc b"]
)
def test_frequency_sort(sol_inst, method_name, s):
    result = getattr(sol_inst, method_name)(s)
    assert is_valid(result, s), f"{method_name}({s!r}) -> {result!r}"


@pytest.mark.parametrize(
    "s",
    ["tree", "cccaaa", "Aabb"]
)
def test_public_api(sol_inst, s):
    assert is_valid(sol_inst.frequencySort(s), s)
