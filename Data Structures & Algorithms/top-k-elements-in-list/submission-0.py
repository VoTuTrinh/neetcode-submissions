class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for x in nums: 
            count[x] += 1
        
        heap = []
        for x in count: 
            heapq.heappush(heap, (count[x], x))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res