import heapq as heap


class KthLargestStream:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.pq = []
        for i in nums:
            self.add(i)

    def add(self, val):
        heap.heappush(self.pq, val)
        if len(self.pq) > self.k + 1:
            heap.heappop(self.pq)
        return self.pq[0]
