class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0,len(height)-1
        leftMax,rightMax = height[l],height[r]
        res = 0

        while l<r:
            if leftMax <rightMax and l<r:
                l+=1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]
                
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        return res



# This code solves the Trapping Rain Water problem. The idea is that water can stay on top of a bar only when there is a taller wall on both sides. For example, in height = [0,2,0,3,1,0,1,3,2,1], the 0 between heights 2 and 3 can hold water because both sides have taller bars. The code uses two pointers, l and r, starting from the leftmost and rightmost bars. l = 0 and r = len(height)-1, so initially l points to height 0 and r points to height 1. Then leftMax stores the tallest bar we have seen from the left, and rightMax stores the tallest bar we have seen from the right. Initially, leftMax = height[l] = 0 and rightMax = height[r] = 1. res = 0 stores the total water collected. The loop while l < r keeps working while the two pointers have not met. The important part is if leftMax < rightMax: if the tallest wall we know on the left is smaller than the tallest wall we know on the right, we move the left pointer because the left side is currently the limiting side. So l += 1 moves l one step right, and leftMax = max(leftMax, height[l]) updates the tallest bar seen from the left. Then res += leftMax - height[l] calculates how much water can sit above the current bar. For example, when l reaches the bar with height 0 after the 2, leftMax is 2, so that position can hold 2 - 0 = 2 units of water. If instead leftMax is greater than or equal to rightMax, the right side is processed: r -= 1 moves the right pointer one step left, rightMax = max(rightMax, height[r]) updates the tallest right-side bar, and res += rightMax - height[r] adds the water above the current right bar. The reason we move the side with the smaller maximum is similar to the Container With Most Water problem: the smaller boundary limits how much water can be trapped. The code keeps moving inward, updating the maximum wall and adding the water at each position. For this example, the trapped water above the bars adds up to 9, so the function finally returns 9.


        