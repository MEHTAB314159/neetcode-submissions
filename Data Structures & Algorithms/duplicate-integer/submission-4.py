class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for n in nums:
            if n in unique_nums:
                return True
            unique_nums.add(n)
        return False




# First, the function `hasDuplicate` receives the list `nums`. Then we create an **empty set** called `unique_nums`. This set is used to remember the numbers that we have already seen. Now the `for` loop takes **one number at a time** from `nums`. For example, if `nums = [1, 2, 3, 3]`, first `n = 1`. The program checks `if 1 in unique_nums`. Since the set is empty, **1 is not there**, so it adds 1 to the set. Now the set is `{1}`. Next, the loop takes `2`. It checks whether 2 is already in the set. It is not, so 2 is added. Now the set is `{1, 2}`. Next, it takes `3`. Again, 3 is not in the set, so it adds 3. Now the set is `{1, 2, 3}`. Then the loop takes **3 again**. This time, `3 in unique_nums` is **True** because we already added 3 earlier. That means we found a **duplicate**, so `return True` immediately stops the function. If the loop checks **all the numbers** and never finds a number that is already in the set, the loop finishes and `return False` is executed, meaning there is **no duplicate**.

# ### 🧠 In one simple sentence:

# **Take a number → check if we have seen it before → if yes, return `True` → if no, add it to the set → continue to the next number → if the whole list finishes, return `False`.**
