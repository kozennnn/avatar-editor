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

    def remove(self, value: int) -> None:
        # if self doesn't exist, just return it
        #if not self:
        #    return self
        # Find the node in the left subtree	if value value is less than self value
        if self.value > value and self.left is not None:
            self.left = self.left.remove(value)
        # Find the node in right subtree if value value is greater than self value,
        elif self.value < value and self.right is not None:
            self.right = self.right.remove(value)
        # Delete the node if self.value == value
        else:
            # If there is no right children delete the node and new self would be self.left
            if not self.right:
                return self.left
            # If there is no left children delete the node and new self would be self.right
            if not self.left:
                return self.right
            # If both left and right children exist in the node replace its value with
            # the minmimum value in the right subtree. Now delete that minimum node
            # in the right subtree
            temp_val = self.right
            mini_val = temp_val.value
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.value
            # Delete the minimum node in right subtree
            self.right = self.right.remove(self.value)
        return self

    def find(self, value: int) -> bool:
        found = False
        if value == self.value:
            found = True
        elif value < self.value:
            if self.left is not None:
                found = self.left.find(value)
        else:
            if self.right is not None:
                found = self.right.find(value)
        return found

    def prefix_course(self):
        parcours = [self.value]
        if self.left is not None:
            parcours.extend(self.left.prefix_course())
        if self.right is not None:
            parcours.extend(self.right.prefix_course())
        return parcours

