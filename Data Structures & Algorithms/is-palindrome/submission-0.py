# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string = ""
#         for c in s:
#             if c.isalnum():
#                 string += c.lower()
#         return string == string[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isALNUM(s[l]):
                l+=1
            while l<r and not self.isALNUM(s[r]):
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True

    def isALNUM(self,c):
        return (ord("A")<=ord(c)<=ord("Z")) or (ord("a")<=ord(c)<=ord("z")) or (ord("0")<=ord(c)<=ord("9"))

