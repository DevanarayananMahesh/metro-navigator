from hash_table import HashTable


class HashSet:
    def __init__(self):
        self._map = HashTable()

    def add(self, item):
        if type(item) is not str:
            raise TypeError
        if self._map.contains(item):
            return False
        self._map.put(item, True)
        return True

    def remove(self, item):
        if type(item) is not str:
            raise TypeError
        
        if not self._map.contains(item):
            raise KeyError
        
        self._map.remove(item)

    def discard(self, item):
        if type(item) is not str:
            raise TypeError
        
        if self._map.contains(item):
            self._map.remove(item)
            return True
        
        return False

    def contains(self, item):
        if type(item) is not str:
            raise TypeError
        
        return self._map.contains(item)

    def __contains__(self, item):
        return self.contains(item)

    def union(self, other):
        if not isinstance(other, HashSet):
            raise TypeError
        
        result = HashSet()

        for item in self.to_list():
            result.add(item)

        for item in other.to_list():
            result.add(item)

        return result

    def intersection(self, other):
        if not isinstance(other, HashSet):
            raise TypeError
        
        result = HashSet()

        for item in self.to_list():
            if item in other:
                result.add(item)

        return result

    def difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError
        
        result = HashSet()

        for item in self.to_list():
            if item not in other:
                result.add(item)

        return result

    def symmetric_difference(self, other):
        if not isinstance(other, HashSet):
            raise TypeError
        
        result = HashSet()

        for item in self.to_list():
            if item not in other:
                result.add(item)

        for item in other.to_list():
            if item not in self:
                result.add(item)

        return result

    def is_subset(self, other):
        if not isinstance(other, HashSet):
            raise TypeError
        
        if len(self) > len(other):
            return False
        
        for item in self.to_list():
            if item not in other:
                return False
            
        return True

    def is_empty(self):
        return len(self._map) == 0

    def clear(self):
        self._map = HashTable()

    def __len__(self):
        return len(self._map)

    def to_list(self):
        return self._map.keys()