class Array:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be > 0")
        self._size = size
        self._elements = [None] * size

    def length(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._elements[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        self._elements[index] = value

    def clearing(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return self._ArrayIterator(self._elements)

    class _ArrayIterator:
        def __init__(self, elements):
            self._elements = elements
            self._index = 0

        def __next__(self):
            if self._index < len(self._elements):
                value = self._elements[self._index]
                self._index += 1
                return value
            raise StopIteration

        def __iter__(self):
            return self
