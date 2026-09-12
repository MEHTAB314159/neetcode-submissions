class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<r:
            Cursum = numbers[l]+numbers[r]

            if Cursum > target:
                r -= 1
            elif Cursum < target:
                l += 1
            else:
                return [l+1,r+1]


# This code solves the Two Sum II problem. We are given a sorted array and a target, and we have to find two different numbers whose sum is equal to the target. For example, if numbers = [1,2,3,4] and target = 3, we need to find 1 + 2 = 3, so the answer is [1,2]. We use two pointers, l and r. l starts at 0, which is the first position in Python, and r starts at len(numbers)-1, which is the last position. We do this because we want to start checking from both ends of the sorted array. The condition while l < r means we keep checking while the two pointers have not met or crossed. Inside the loop, Cursum = numbers[l] + numbers[r] adds the two numbers currently pointed to by l and r. If Cursum > target, the sum is too big, so we need a smaller number. Because the array is sorted, we move the right pointer toward the left using r -= 1. If Cursum < target, the sum is too small, so we need a bigger number, and because the array is sorted, we move the left pointer toward the right using l += 1. If the sum is exactly equal to the target, we have found the two numbers, so we return [l+1, r+1]. We add 1 because the question wants the answer in 1-based indexing, while Python uses 0-based indexing. For [1,2,3,4], Python indexes are 0,1,2,3, but the question considers the positions as 1,2,3,4.