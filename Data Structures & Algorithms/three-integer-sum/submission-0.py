class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l,r = i+1,len(nums)-1
            while l<r:
                ThreeSum = a + nums[l] + nums[r]
                if ThreeSum > 0:
                    r -=1
                elif ThreeSum < 0:
                    l +=1
                else:
                    res.append([a,nums[l],nums[r]])

                    # bxc  here we need to change triple value to find more number == 0 so if we incremnt only ome value i.e l and then checlk the vlaue of triplet then it would not be same as previous one,so then wen caan get possiblke solution

                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res




# This code solves the 3Sum problem, where we have to find three different numbers whose sum is 0, and we must not return duplicate triplets. First, res = [] creates an empty list to store our answers, and nums.sort() sorts the numbers from smallest to largest. Then for i, a in enumerate(nums) chooses one number a at a time as the first number of our triplet. The condition if i > 0 and a == nums[i-1]: continue skips a if the same number was already used before, because otherwise we could get the same triplet again. After choosing a, we set l = i + 1 and r = len(nums) - 1. We use i + 1 for l because a is already being used, so we need two different numbers after it, and r starts at the last position of the array. The while l < r loop keeps searching while l and r are at different positions. We calculate ThreeSum = a + nums[l] + nums[r]. If the sum is greater than 0, it means the sum is too big, so because the array is sorted, we move r left using r -= 1 to get a smaller number. If the sum is less than 0, it means the sum is too small, so we move l right using l += 1 to get a bigger number. If the sum is exactly 0, we have found a correct triplet, so we add [a, nums[l], nums[r]] to res. After finding a triplet, we do l += 1 because we want to move to the next number and search for another possible triplet. Then while l < r and nums[l] == nums[l-1] checks whether the new number is the same as the previous number. If it is the same, we keep moving l forward because using that same number again could create the same triplet, which the question does not allow. This duplicate-checking while is not looking for a sum; the sum has already been found, and this part only skips repeated numbers. We don't use r -= 1 here because this particular NeetCode solution handles the duplicate values by moving l forward. Finally, when all possible values of a have been checked, return res gives us all the unique triplets.

# 🧠 Easy way to remember

# Choose a → use l and r → check sum → move pointer → save answer → skip duplicates.

# And the most important rule is:

# Sum too big → r--
# Sum too small → l++
# Sum = 0 → save it, then move l and skip duplicates.

