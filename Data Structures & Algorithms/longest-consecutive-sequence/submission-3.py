class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest


# The code works by first doing numSet = set(nums), which converts the list into a set: {100, 4, 200, 1, 3, 2}. We use a set because checking whether a number exists in it is very fast. Then longest = 0 means that currently our longest sequence has length 0. Now for n in nums takes one number at a time. For n = 100, the code checks if (n - 1) not in numSet, which means "Is 99 not in the set?" Yes, 99 is not there, so 100 could be the beginning of a sequence. We set length = 0, then the while checks whether n + length is in the set. For 100, 100 + 0 = 100, which exists, so length becomes 1. Then it checks 101, which doesn't exist, so the loop stops. longest = max(1, 0) gives 1. Next n = 4. We check whether 3 is in the set. Yes, 3 exists, so 4 is not the beginning of a sequence, and we skip it. Next n = 200. We check whether 199 exists. It doesn't, so 200 is considered a starting point. The while loop finds 200, so its length is 1, and longest stays 1. Next n = 1. We check whether 0 exists. It doesn't, so 1 is the beginning of a sequence. Now the while loop starts checking consecutive numbers: 1 + 0 = 1 exists, so length = 1; then 1 + 1 = 2 exists, so length = 2; then 1 + 2 = 3 exists, so length = 3; then 1 + 3 = 4 exists, so length = 4; finally 1 + 4 = 5 does not exist, so the loop stops. Now longest = max(4, 1), so longest becomes 4. Then n = 3 is checked, but 2 is already in the set, so 3 is not the beginning and we skip it. Finally n = 2; 1 is already in the set, so we skip it. After checking everything, return longest returns 4.
