import pytest
from Sort.e147_Insertion_Sort_list import Solution, ListNode


def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


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
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]
)
def test_insert(sol_inst, list_vals, res_vals):
    head = build_list(list_vals)
    result = sol_inst.insertionSortList(head)
    assert to_array(result) == res_vals
