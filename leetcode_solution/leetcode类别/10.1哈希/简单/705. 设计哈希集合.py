# 设计哈希集合,只是list唯一

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.set

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)