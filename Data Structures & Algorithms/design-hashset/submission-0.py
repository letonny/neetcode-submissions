class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]  # list of lists

    def _hash(self, key):
        return key % self.bucket_size

    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]
