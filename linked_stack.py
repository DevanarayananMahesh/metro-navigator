from linked_list import LinkedList


class Stack:

    def __init__(self):
        self._list = LinkedList()

    def push(self, item):
        self._list.prepend(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._list.remove_at(0)

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self._list.get(0)

    def is_empty(self):
        return len(self._list) == 0

    def clear(self):
        self._list.clear()

    def to_list(self):
        return self._list.to_list()

    def __len__(self):
        return len(self._list)


def is_balanced(text):
    if not isinstance(text, str):
        raise TypeError

    stack = Stack()
    matching_pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_pairs[char]:
                return False

    return stack.is_empty()