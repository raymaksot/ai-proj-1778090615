import pytest
from main import BinarySearchTree


def test_insert_and_search():
    """Test insertion and search functionality."""
    bst = BinarySearchTree()
    # initially tree is empty, search should return False
    assert bst.search(10) is False

    # insert values
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)

    # search existing values
    assert bst.search(30) is True
    assert bst.search(70) is True
    # search non-existing value
    assert bst.search(100) is False


def test_inorder_traversal():
    """Test inorder traversal returns sorted list."""
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for v in values:
        bst.insert(v)
    result = bst.inorder()
    expected = sorted(values)
    assert result == expected


def test_preorder_traversal():
    """Test preorder traversal after known insertions."""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    # Preorder should be root, left subtree, right subtree
    expected = [5, 3, 2, 4, 7, 6, 8]
    assert bst.preorder() == expected


def test_postorder_traversal():
    """Test postorder traversal after known insertions."""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    # Postorder should be left subtree, right subtree, root
    expected = [2, 4, 3, 6, 8, 7, 5]
    assert bst.postorder() == expected


def test_empty_tree_traversals():
    """All traversals on an empty tree should return empty lists."""
    bst = BinarySearchTree()
    assert bst.inorder() == []
    assert bst.preorder() == []
    assert bst.postorder() == []


def test_duplicate_insertion():
    """Inserting duplicate values should not change the tree."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    bst.insert(10)
    # inorder should contain only one copy
    assert bst.inorder() == [10]
    # search should still find it
    assert bst.search(10) is True


def test_single_node_tree():
    """Tree with a single node should behave correctly."""
    bst = BinarySearchTree()
    bst.insert(42)
    assert bst.search(42) is True
    assert bst.search(24) is False
    assert bst.inorder() == [42]
    assert bst.preorder() == [42]
    assert bst.postorder() == [42]