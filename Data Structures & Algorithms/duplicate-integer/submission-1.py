# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
        

class Solution:
    def hasDuplicate(self, nums):
        # number = []
        # for n in nums:
        #     if n not in number:
        #         number.append(n)
        #     else:
        #         return True
        # return False
        number = []
        for n in nums:
            if n not in number:
                number.append(n)
            else:
                return True
        return False
