"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

"""


class MinStack(object):

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self._stack:
            item = self._stack.pop()
            if self._min_stack and item == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self._min_stack:
            return self._min_stack[-1]
        return None


if __name__ == "__main__":
    obj = MinStack()
    for num in range(1, 6):
        obj.push(num)
    obj.pop()
    assert obj.top() == 4
    assert obj.getMin() == 1
