# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
class Solution:
    def productExceptSelf(self,nums):
        ans = [1]*len(nums)
        # print(ans)

        for i in range(1,len(nums)):
            # print(i)
            ans[i] = nums[i-1]*ans[i-1]
            # print(ans)

        rightproduct = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i] = rightproduct * ans[i]
            rightproduct = rightproduct * nums[i]
            # print(ans)
        return ans


      