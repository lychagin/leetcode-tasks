import pytest
from Tree.e94_Binary_Tree_Inorder_Traversal import Solution
from Tree.util import TreeNode

@pytest.fixture
def sol_inst():
    return Solution()

@pytest.mark.parametrize(
    "values, target, res",
    [
        ([1, None, 2, 3], None, [1, 3, 2]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], None, [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        ([], None, []),
        ([1], None, [1]),
        ([2, 1, 3], None, [1, 2, 3]),
        ([1, None, 2, None, 3], None, [1, 2, 3]),
    ]
)
def test_inorderTraversal(sol_inst, values, target, res):
    tree = TreeNode.fromList(values) if values else None
    assert sol_inst.inorderTraversal(tree) == res
