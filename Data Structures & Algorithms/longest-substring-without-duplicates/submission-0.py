class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res

# `if` → Check a condition **once** and do something if it is true.
# `else` → Do something **when the `if` condition is false**.
# `for` → Repeat/visit **each item or index** in a sequence.
# `while` → Keep repeating **as long as the condition is true**.


# This code finds the length of the longest substring without repeating characters. First, charSet = set() creates an empty set to store the characters currently inside our window, l = 0 makes the left pointer start at index 0, and res = 0 stores the biggest length found so far. Then for r in range(len(s)) makes the right pointer r move from left to right through every character. For each character, while s[r] in charSet checks whether the current character is already present; if it is a duplicate, charSet.remove(s[l]) removes the character at the left pointer and l += 1 moves the left pointer one step right. The while keeps doing this until the duplicate is removed. Then charSet.add(s[r]) adds the current character to the set, and res = max(res, r-l+1) calculates the current window length and keeps the larger answer. Finally, return res gives the longest length. For example, with "abcabcbb", the window grows to "abc" with length 3; when another a, b, or c appears, l moves forward until the duplicate is gone, while r continues moving forward. So the final answer is 3.

# 🧠 Easy memory: r moves forward → duplicate? → l moves forward → add character → calculate length.