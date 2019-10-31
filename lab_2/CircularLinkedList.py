import math


def prime(n):
    if n < 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


# List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
            string = string + str(curr.value) + " "
            curr = curr.next
        string = string + str(curr.value)
        return string



    def task(self):
        if self.head is None:
            raise IOError()
        curr = self.head
        try:
            # увеличиваем на 3
            while curr.next is not self.head:
                curr.value += 3
                curr = curr.next
            curr.value += 3

            # убираем простые
            old = self.head
            curr = self.head.next

            while old.next is not self.head:
                if prime(curr.value) is True:
                    old.next = curr.next
                old = old.next
                curr = old.next

            if (prime(curr.value) and (self.head.next is not self.head)) is True:
                old.next = curr.next
                self.head = curr.next
            elif prime(curr.value) is True:
                self.head = None

        except IOError:
            raise IOError()
        except Exception:
            raise Exception("Неверные входные параметры")





