class HashTableLP:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __setitem__(self, key, value):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def __getitem__(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        raise KeyError(key)

    def __delitem__(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.rehash()
                return
            index = (index + 1) % self.size

        raise KeyError(key)

    def hash(self, key):
        return hash(key) % self.size

    def rehash(self):
        new_keys = [None] * self.size
        new_values = [None] * self.size

        for i in range(self.size):
            if self.keys[i] is not None:
                index = self.hash(self.keys[i])
                while new_keys[index] is not None:
                    index = (index + 1) % self.size
                new_keys[index] = self.keys[i]
                new_values[index] = self.values[i]

        self.keys = new_keys
        self.values = new_values
