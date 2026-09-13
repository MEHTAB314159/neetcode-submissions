class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0,len(heights)-1
        while l<r:
            area = (r-l)*min(heights[l],heights[r])
            res = max(res,area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res



# This code finds the maximum amount of water that can be stored between two bars. It uses two pointers, l and r, starting from the two ends of the array. For your example, heights = [1,7,2,5,4,7,3,6], the indexes are 0,1,2,3,4,5,6,7. First, res = 0 means we have not found any area yet. Then l = 0 and r = len(heights)-1, so l = 0 points to height 1, and r = 7 points to height 6. The while l < r loop means we keep checking while the two pointers have not met. In the first round, area = (r-l) * min(heights[l], heights[r]), so the width is 7-0 = 7, the smaller height is min(1,6) = 1, and the area is 7*1 = 7. Then res = max(res, area) compares our current answer 0 with 7, so res becomes 7. Next, the code checks if heights[l] < heights[r]. Since 1 < 6 is true, we move the left pointer one step right using l += 1, because the left bar is shorter and is limiting the amount of water. Now l = 1 and r = 7, so the heights are 7 and 6. The width is 7-1 = 6, and the smaller height is 6, so the area is 6*6 = 36. res becomes 36 because 36 is bigger than 7. Now heights[l] < heights[r] means 7 < 6, which is false, so the else runs and r -= 1, moving the right pointer one step left. Now l = 1 and r = 6, giving heights 7 and 3. The area is (6-1) * min(7,3) = 5*3 = 15, so res stays 36. Since 3 is smaller than 7, r moves left again. The code keeps doing the same thing: calculate the area, keep the larger area in res, and move the pointer belonging to the shorter bar. Eventually the pointers meet, l < r becomes false, and the loop stops. The final res is 36, so the answer is 36.
        
        