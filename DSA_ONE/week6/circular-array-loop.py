class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        leng = len(nums)
        count = 0

        for i in range(leng):
            l=(i+nums[i] )% leng
            ind=i
            condition = None
            count+=1
            visited = set()
            if nums[ind] >0:
                condition = True
            else:
                condition = False
            while i != l:
                if  l in visited:
                    condition = None
                    break
                if (nums[l] > 0 and condition) or (nums[l] < 0 and not condition) :
                    visited.add(ind)
                    visited.add(l)
                    # print(ind,l)
                    ind=l
                    l= (nums[ind] + l) %leng
                    # visited.add(l)
                    count+=1
                else:
                    condition = None
                    break
            # print(visited,"_____")
            # print(condition,count)
            if condition != None and count > 1:
                return True
            count = 0
        return False
                



                
        