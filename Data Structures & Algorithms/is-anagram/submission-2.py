class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
    
        return True




# Suppose the input is `s = "racecar"` and `t = "carrace"`. The purpose of this program is to check whether both strings are **anagrams**, which means they must contain the **same letters the same number of times**, even if their order is different. First, the function receives `s` and `t`, and it checks whether their lengths are equal. If their lengths are different, it immediately returns `False` because two strings with different lengths cannot have exactly the same letters. If the lengths are equal, the program creates two empty dictionaries, `countS` and `countT`. Think of these dictionaries as **two notebooks for counting letters**—one notebook for `s` and one for `t`. Then the first `for` loop goes through both strings one position at a time. The important line is `countS[s[i]] = 1 + countS.get(s[i], 0)`. Here, `s[i]` means the **current letter**. For example, when `i = 0`, `s[0]` is `r`, so the line becomes `countS['r'] = 1 + countS.get('r', 0)`. Because `r` is not in the dictionary yet, `.get('r', 0)` gives `0`, so `1 + 0 = 1`, and the dictionary stores `r: 1`. When `r` appears again later, `.get('r', 0)` finds the old count `1`, so `1 + 1 = 2`, and the dictionary changes to `r: 2`. This is how the program **counts how many times each letter appears**. The same process happens for `countT` using the letters of `t`. After the first loop, we get `countS = {'r': 2, 'a': 2, 'c': 2, 'e': 1}` and `countT = {'c': 2, 'a': 2, 'r': 2, 'e': 1}`. Then comes the second `for` loop: `for c in countS:`. Here, **`c` is only a variable name; it does not mean the letter `c`**. Python takes each key from `countS` one by one and temporarily puts it inside `c`. So first `c = 'r'`, then `c = 'a'`, then `c = 'c'`, and then `c = 'e'`. When `c = 'r'`, the condition `countS[c] != countT[c]` becomes `countS['r'] != countT['r']`, so it compares the count of `r` in both dictionaries. Both are `2`, so it continues. Then it checks `a`, then `c`, then `e`. Notice that Python is **not assuming that both dictionaries have the same letters**; it takes a letter from `countS` and checks that **exact same letter** in `countT`. If any letter has a different count, `return False` is executed. If every letter has the same count, the loop finishes and `return True` is executed. Therefore, for `"racecar"` and `"carrace"`, all the letter counts match, so the answer is `True`.

# ### 🧠 The whole question in one flow

# **Check length → make two counting dictionaries → first loop counts letters → `.get()` gives old count → add 1 → second loop compares the same letters → different count = `False` → everything same = `True`.**

# And remember the most important line:

# ```python
# countS[s[i]] = 1 + countS.get(s[i], 0)
# ```

# means:

# **Current letter → find its old count → add 1 → save the new count.**

# And:

# ```python
# for c in countS:
# ```

# means:

# **Take each letter/key from `countS` one by one; `c` is just the temporary variable holding that letter.**


# What is .get()?
# .get() is a dictionary method. It is used when we want to get the value of a particular key from a dictionary.
