class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = []
        for n in nums:
            if n not in number:
                number.append(n)
            else:
                return True
        return False
        
