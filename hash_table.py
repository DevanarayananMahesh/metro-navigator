class HashNode:
    """A node in a hash table bucket chain.

    Attributes:
        key: String key for hashing and lookup.
        value: Data payload linked to the key.
        next: Pointer to the next node in the collision chain.
    """

    def __init__(self, key, value):
        """Initializes a bucket chain node.

        Args:
            key: Key string.
            value: Associated value payload.
        """
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """A separate-chaining hash table.

    Attributes:
        capacity: Current total number of bucket slots.
        _size: Number of key-value pairs stored.
        buckets: List holding the linked list chain heads.
    """

    def __init__(self):
        """Sets up an empty hash table with 8 initial buckets."""
        self.capacity = 8
        self._size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        """Computes the bucket index for a key string.

        Args:
            key: The string key to hash.

        Returns:
            An integer bucket index within self.capacity limits.
        """
        p = 31
        hash_val = 0
        for char in key:
            hash_val = hash_val * p + ord(char)
        return hash_val % self.capacity

    def load_factor(self):
        """Calculates current load ratio.

        Returns:
            Float representing size divided by capacity.
        """
        return self._size / self.capacity

    def _resize(self):
        """Doubles bucket capacity and re-hashes existing items."""
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
        """Inserts a key-value pair or updates existing key.

        Args:
            key: Target string key.
            value: Data to store.

        Raises:
            TypeError: If key is not a string.
        """
        if type(key) is not str:
            raise TypeError("Key must be a string.")

        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self._size += 1

        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key, default=None):
        """Retrieves value for a key string.

        Args:
            key: Key string to lookup.
            default: Fallback value if key isn't found.

        Returns:
            The stored value or the default fallback.

        Raises:
            TypeError: If key is not a string.
        """
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
        """Deletes a key-value entry from the table.

        Args:
            key: Key string to remove.

        Returns:
            The value attached to the removed key.

        Raises:
            TypeError: If key is not a string.
            KeyError: If key doesn't exist.
        """
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
        """Checks if a key exists in the table.

        Args:
            key: Key string to check.

        Returns:
            True if key is present, False otherwise.

        Raises:
            TypeError: If key is not a string.
        """
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
        """Gathers all active keys in the hash table.

        Returns:
            A list containing every stored key string.
        """
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append(curr.key)
                curr = curr.next
        return out

    def values(self):
        """Gathers all values stored in the hash table.

        Returns:
            A list containing every value payload.
        """
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append(curr.value)
                curr = curr.next
        return out

    def items(self):
        """Gathers all key-value tuples stored in the table.

        Returns:
            A list of (key, value) tuple pairs.
        """
        out = []
        for head in self.buckets:
            curr = head
            while curr is not None:
                out.append((curr.key, curr.value))
                curr = curr.next
        return out

    def __getitem__(self, key):
        """Allows dict-like bracket indexing for retrieving values."""
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
        """Allows dict-like bracket assignment (table[key] = val)."""
        self.put(key, value)

    def __delitem__(self, key):
        """Allows dict-like key deletion (del table[key])."""
        self.remove(key)

    def __contains__(self, key):
        """Enables 'in' operator syntax."""
        return self.contains(key)

    def __len__(self):
        """Returns the total number of items stored."""
        return self._size