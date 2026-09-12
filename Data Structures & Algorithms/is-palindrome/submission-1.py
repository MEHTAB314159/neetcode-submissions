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


# Explanation in simple passage form

# This code checks whether a given string is a palindrome. A palindrome is a word or sentence that reads the same from the front and from the back, while ignoring spaces, punctuation, and capital letters. For example, "Was it a car or a cat I saw?" is a palindrome because, after ignoring spaces and ? and converting everything to lowercase, it becomes "wasitacaroracatisaw", which is the same forward and backward. The code uses two pointers, l and r. l starts at the first character using l = 0, and r starts at the last character using r = len(s) - 1. The while l < r loop means that we keep checking characters from both sides until the pointers meet or cross. The first inner while moves l forward if the character is not a letter or number, such as a space or ?. The second inner while moves r backward for the same reason. After finding two valid characters, the code compares them using .lower() so that uppercase and lowercase are treated as the same. If they are different, the code immediately returns False. If they are the same, l moves one step right with l + 1, and r moves one step left with r - 1, and the process continues. If all the characters match, the loop finishes and the code returns True. The isAlNUM() function is used to check whether a character is an uppercase letter, lowercase letter, or number by comparing its ASCII value using ord().

# What you were having difficulty understanding

# Your main difficulty was understanding what the two pointers are doing and why they move in opposite directions. You understood that l = 0 means the first position and r = len(s) - 1 means the last position, but it was confusing why we use while l < r, why we skip spaces and symbols, and why r must use r - 1 instead of r + 1. The important idea is simply to imagine two people checking a word from opposite ends: l walks from left to right, and r walks from right to left. They compare the outside characters first, then move closer to the middle. You also had a small confusion about l, r = 0, len(s)-1; this is just a short way of writing l = 0 and r = len(s)-1. Finally, the isAlNUM() function may look complicated because of ord(), but its only job is to say “Is this character a letter or a number?” Once you understand these three ideas—two pointers, skip unwanted characters, compare from both sides—the whole problem becomes much easier.
