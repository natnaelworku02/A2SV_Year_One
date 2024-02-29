class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                val = stack.pop()
                if stack:
                    _min = min(height[i],height[stack[-1]])
                    # print(height[i],height[stack[-1]])
                    d = i  - stack[-1] - 1
                    # print(d)
                    # print(val,"hi")
                    ans += (_min - height[val]) * d
                    # print((_min - val) * d)
                    # print(ans,_min,val,i)

            stack.append(i)
        
        return ans