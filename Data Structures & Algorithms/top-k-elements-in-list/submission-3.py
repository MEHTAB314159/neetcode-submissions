class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        frequency = [[] for i in range(len(nums)+1)]
        for n,c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res



# Suppose nums = [1, 1, 1, 2, 2, 100] and k = 2. The question asks us to find the 2 numbers that appear most frequently, so the answer will be [1, 2]. First, the program creates an empty dictionary count = {}. This dictionary is like a notebook where we store each number as the key and its frequency as the value. The first for loop takes each number from nums one by one and counts it using count[n] = 1 + count.get(n, 0). For the first 1, it is not in the dictionary, so .get(1, 0) gives 0, and 1 + 0 = 1, so we store 1:1. When another 1 comes, its old count is 1, so 1 + 1 = 2; when the third 1 comes, its count becomes 3. Similarly, 2 gets a count of 2, and 100 gets a count of 1. At the end, count becomes {1: 3, 2: 2, 100: 1}, which means 1 appeared 3 times, 2 appeared 2 times, and 100 appeared 1 time. Next, the program creates frequency = [[] for i in range(len(nums) + 1)]. These are empty buckets, and the bucket number represents how many times a number appeared. Since there are 6 elements, we create 7 buckets so that we can have frequency[0] through frequency[6]. Then the second for loop for n, c in count.items() takes one key-value pair at a time from count. Here, n means the number and c means its count. So for 1:3, n = 1 and c = 3. The line frequency[c].append(n) then means put the number n inside the bucket whose number is its frequency c. Therefore, 1 goes into frequency[3], 2 goes into frequency[2], and 100 goes into frequency[1]. Now our buckets look like frequency[3] = [1], frequency[2] = [2], and frequency[1] = [100]. After that, we create res = [], which is our empty answer list. The next loop for i in range(len(frequency) - 1, 0, -1) starts from the highest frequency and moves backwards, because we want the most frequent numbers first. It checks frequency[6], frequency[5], frequency[4], then frequency[3], where it finds 1, so res.append(1) makes res = [1]. Then it reaches frequency[2], where it finds 2, so res.append(2) makes res = [1, 2]. Now len(res) == k because k = 2, so the program immediately returns [1, 2]. The last return [] is simply a fallback in case no answer is found.

# 🧠 Remember the complete flow:

# Count → Put numbers into frequency buckets → Start from the highest-frequency bucket → Take numbers until k numbers are collected → Return the result.

       