"""

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

"""
import random


class RandomizedSet:

    def __init__(self):
        self._list = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        self._dict[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False
        list_index = self._dict[val]
        last_value = self._list[-1]
        self._list[list_index], self._list[-1] = self._list[-1], self._list[list_index]
        self._list.pop()
        self._dict[last_value] = list_index
        del self._dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._list)


if __name__ == "__main__":
    obj = RandomizedSet()
    for i in range(1, 6):
        status = obj.insert(i)
        assert status

    assert obj.remove(5)
    assert not(obj.remove(5))
    assert obj.getRandom() in {1, 2, 3, 4}
