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
