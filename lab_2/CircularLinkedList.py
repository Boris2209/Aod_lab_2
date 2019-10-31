# List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def returnValue(self):
        return self.value


class CircularLinkedList:
    def __init__(self):
        self.head = None     # First element

    def append(self, value):
        """ New elements """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next
            node.next = self.head
            curr.next = node

    def get_list(self):
        if self.head is None:
            return "Нет элементов"
        string = ""
        curr = self.head
        while curr.next is not self.head:
            string = string + str(curr.returnValue()) + " "
            curr = curr.next
        string = string + str(curr.returnValue())
        return string



