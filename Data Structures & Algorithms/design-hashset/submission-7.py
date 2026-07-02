class MyHashSet:

    def __init__(self):
        self.data_size = 10000
        self.data = [[] for i in range(self.data_size)]

    def add(self, key: int) -> None:
        h = key % self.data_size
        if key not in self.data[h]:
            self.data[h].append(key)

    def remove(self, key: int) -> None:
        h = key % self.data_size
        if key in self.data[h]:
            self.data[h].remove(key)

    def contains(self, key: int) -> bool:
        h = key % self.data_size
        return key in self.data[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)