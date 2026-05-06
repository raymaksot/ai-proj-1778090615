from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    """Node in a binary search tree."""
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None


class BinarySearchTree:
    """Binary Search Tree with insertion, search and three traversals."""

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """Insert a value into the BST."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # if equal, do nothing (no duplicates)
        return node

    def search(self, value: int) -> bool:
        """Return True if value exists in the tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: int) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self) -> List[int]:
        """Return list of values from inorder traversal."""
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self) -> List[int]:
        """Return list of values from preorder traversal."""
        result: List[int] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self) -> List[int]:
        """Return list of values from postorder traversal."""
        result: List[int] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


def main() -> None:
    """Demonstrate BST operations and traversals."""
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Binary Search Tree Traversals")
    print(f"Inserted values: {values}")
    print(f"In-order:    {bst.inorder()}")
    print(f"Pre-order:   {bst.preorder()}")
    print(f"Post-order:  {bst.postorder()}")

    # Demonstrate search
    search_values = [40, 90]
    for sv in search_values:
        found = bst.search(sv)
        print(f"Search {sv}: {'Found' if found else 'Not found'}")


if __name__ == "__main__":
    main()