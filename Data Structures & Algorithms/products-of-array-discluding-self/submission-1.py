class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# This productExceptSelf code finds the product of all the numbers except the number at the current position, without using division. The main idea is to calculate the product in two directions: first from the left using prefix, and then from the right using postfix. Suppose nums = [1, 2, 3, 4]. First, res = [1] * len(nums) creates [1, 1, 1, 1], because res will store the final answers. We start with prefix = 1. In the first loop, we move from left to right. At index 0, res[0] *= prefix, so res[0] stays 1, and then prefix *= nums[0], so prefix becomes 1. At index 1, res[1] *= prefix, so it gets 1, and then prefix becomes 1 × 2 = 2. At index 2, res[2] gets 2, and then prefix becomes 2 × 3 = 6. At index 3, res[3] gets 6, and then prefix becomes 6 × 4 = 24. So after the first loop, res = [1, 1, 2, 6]. These values represent the product of everything to the left of each position. Now we start postfix = 1 and go from right to left using range(len(nums)-1, -1, -1), which gives indexes 3, 2, 1, 0. At index 3, there is nothing to the right, so we multiply res[3] by 1, and then postfix becomes 1 × 4 = 4. At index 2, res[2] currently contains 2, so we multiply it by 4, giving 8; then postfix becomes 4 × 3 = 12. At index 1, res[1] becomes 1 × 12 = 12; then postfix becomes 12 × 2 = 24. Finally, at index 0, res[0] becomes 1 × 24 = 24. So the final answer is [24, 12, 8, 6]. In simple words, the first loop puts the product of everything on the left into res, and the second loop multiplies it by everything on the right. This gives us the product of every number except itself. Your second solution uses the total product and division, but it fails when there is 0, because you cannot divide by zero. The prefix/postfix solution is better because it does not use division and correctly handles zeros.

        
      










      


# this code is valid only when there is no zero in the code,so this is not optimal solution
# class Solution:
#     def productExceptSelf(self, nums):
#         product = 1
#         for n in nums:
#             product *= n
#         result = []
#         for n in nums:
#             result.append(product // n)
#         return result