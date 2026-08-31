class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        topk  = sorted(d,key = d.get,reverse = True)
        return topk[:k]

# # key = d.get ===>sort according to frequency
# # reverse = True ===>put the higest frequency first
# # [2, 3, 1][:2]

        