import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            count = [0]*26

            for letter in s:
                count[ord(letter)-ord("a")] += 1

            d[tuple(count)].append(s)
        return list(d.values())



# why tuple count
# A list cannot be used as a dictionary key.
# Sure 😊 Let’s understand the **complete Group Anagrams program** in very simple English, step by step, in one passage.

# Suppose our input is `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`. The purpose of this program is to put words that have the **same letters** into the same group. First, we import `collections` because we are going to use `defaultdict`. Then we create `d = collections.defaultdict(list)`. Think of `d` as a set of **boxes**, where each box will contain words that are anagrams of each other. The `list` means that whenever a new key is created, Python will automatically give that key an empty list `[]` where we can store words. Then the outer `for` loop takes one word at a time from `strs`. Suppose the first word is `"eat"`. We create `count = [0] * 26`, which gives us a list of 26 zeros, one position for every English alphabet letter. Then the inner `for` loop takes each letter from `"eat"` one by one. For each letter, `ord(letter) - ord("a")` finds the position of that letter in the alphabet. For example, `a` gives position `0`, `e` gives position `4`, and `t` gives position `19`. Then `count[...] += 1` increases the number at that position, so the program is counting how many times each letter appears. After checking `"eat"`, the `count` list represents that `a`, `e`, and `t` appear once. We then use `tuple(count)` as the **key** because a tuple can be used as a dictionary key. The line `d[tuple(count)].append(s)` means **"find the box belonging to this letter-count pattern and put the current word `s` inside it."** Since `"eat"` is the first word with this pattern, Python creates an empty list and puts `"eat"` inside it. When the program later reaches `"tea"`, its letters are counted and produce the **exact same count pattern**, even though the letters are in a different order. Therefore, it gets the same key and `.append(s)` puts `"tea"` into the same list, making `["eat", "tea"]`. When `"ate"` comes, it has the same pattern again, so it is also added to that group. Similarly, `"tan"` and `"nat"` have another matching pattern, so they go into another group, while `"bat"` gets its own group. Finally, `return list(d.values())` takes all the lists from the dictionary and returns them, giving groups such as `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`.

# ### 🧠 Easy way to remember:

# **Take a word → count its letters → make that count the key → put the word into that key's list → words with the same letter counts automatically come into the same group.**
