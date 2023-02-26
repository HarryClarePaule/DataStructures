# print(ord('a'))
# https://docs.python.org/3/library/operator.html operators found here

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self. arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                idx = (key,val)
                self.arr[h][idx]
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print(f'Deleted {key} entry')
                del self.arr[h][index]


h = HashTable()

print(get_hash('march'))
print(get_hash('archm'))
print('Break')
h['june 7'] = 207 # uses the '__setitem__' function python operator
h['march 10'] = 400
h['sept 20'] = 500
h['aug 21'] = 321
h['march 6'] = 321
h['archm 6'] = 439

print(h.arr)
print('Break')
print(h['june 7']) # usees the '__getitem' function python operator
print('Break')

print(h.arr)
print(h['archm 6'])
print(h['march 6'])
del h['march 6']
print(h.arr)




