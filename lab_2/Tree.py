from math import fabs

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.result = ""

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        else:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

    def print_tree(self):
        self.result = ""
        if self.root is not None:
            self._print_tree(self.root)
        return self.result

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            self.result += ((str(cur_node.value))+" ")
            self._print_tree(cur_node.right)

    def task(self):
        if self.root is not None:
            self._task(self.root)

    def _task(self, cur_node):
        if cur_node is not None:
            self._task(cur_node.left)
            cur_node.value = int(fabs(cur_node.value))
            self._task(cur_node.right)


