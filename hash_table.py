class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 8
        self._size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        p = 31
        hash_val = 0
        for char in key:
            hash_val = hash_val * p + ord(char)
        return hash_val % self.capacity

    def load_factor(self):
        return self._size / self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self._size = 0

        for head in old_buckets:
            current = head
            while current is not None:
                self.put(current.key, current.value)
                current = current.next

    def put(self, key, value):
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]

        # Update existing key
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Insert new key at the head of the chain
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node # type: ignore
        self._size += 1

        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key, default=None):
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return default

    def remove(self, key):
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return current.value

            prev = current
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def contains(self, key):
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return True
            current = current.next

        return False

    def keys(self):
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append(curr.key)
                curr = curr.next
        return out

    def values(self):
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append(curr.value)
                curr = curr.next
        return out

    def items(self):
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append((curr.key, curr.value))
                curr = curr.next
        return out

    def __getitem__(self, key):
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self._size