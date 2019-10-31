class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.rigth = None


class Tree:
    def __init__(self):
        self.root = None

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
            if cur_node.rigth is None:
                cur_node.rigth = Node(value)
            else:
                self._insert(value, cur_node.rigth)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.rigth)


T = Tree()
T.insert(1)
T.insert(1)
T.insert(1)
T.insert(4)
T.insert(5)

T.print_tree()


