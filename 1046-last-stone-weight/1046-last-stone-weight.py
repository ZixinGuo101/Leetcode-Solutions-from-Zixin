class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapify_max(maxheap)

        while len(maxheap) >= 2:
            y = heappop_max(maxheap)
            x = heappop_max(maxheap)
            if y - x == 0:
                continue
            heappush_max(maxheap, y - x)
        return maxheap[0] if len(maxheap) > 0 else 0