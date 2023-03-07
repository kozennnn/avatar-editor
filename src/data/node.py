from typing import Self


class Node:
    def __init__(self, value: int, left: Self | None = None, right: Self | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    @property
    def size(self) -> int:
        count = 1
        if self.left is not None:
            count += self.left.size
        if self.right is not None:
            count += self.right.size
        return count

    @property
    def height(self) -> int:
        left = 0
        right = 0
        if self.left is not None:
            left = self.left.height
        if self.right is not None:
            right = self.right.height
        return 1 + max(left, right)

    def insert(self, value: int) -> None:
        tree = self
        while tree is not None:
            if value == tree.value:
                tree = None
            elif value < tree.value:
                if tree.left is None:
                    tree.left = Node(value=value)
                    tree = None
                else:
                    tree = tree.left
            else:
                if tree.right is None:
                    tree.right = Node(value=value)
                    tree = None
                else:
                    tree = tree.right

    def prefix_course(self):
        parcours = [self.value]
        if self.left is not None:
            parcours.extend(self.left.prefix_course())
        if self.right is not None:
            parcours.extend(self.right.prefix_course())
        return parcours

