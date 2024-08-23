"""

The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Answers within 10^-5 of the actual answer will be accepted.

"""
import heapq


class MedianFinder:

    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self._max_heap, -num)

        if self._max_heap and self._min_heap and (-self._max_heap[0] > self._min_heap[0]):
            heapq.heappush(self._min_heap, -heapq.heappop(self._max_heap))

        if len(self._max_heap) > len(self._min_heap) + 1:
            heapq.heappush(self._min_heap, -heapq.heappop(self._max_heap))
        elif len(self._min_heap) > len(self._max_heap):
            heapq.heappush(self._max_heap, -heapq.heappop(self._min_heap))

    def findMedian(self) -> float:
        if len(self._max_heap) == len(self._min_heap):
            return (-self._max_heap[0] + self._min_heap[0]) / 2
        return -self._max_heap[0]


if __name__ == "__main__":
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0
