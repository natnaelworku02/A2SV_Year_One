class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        nums = []
        for i in range(len(difficulty)):
            nums.append([difficulty[i],profit[i]])
        # print(nums)
        nums.sort()
        print(nums)

        worker.sort()
        print(worker)
        ind = 0
        ans = [0]
        for person in worker:
            temp = 0
            flag = False
            while ind < len(nums) and person >= nums[ind][0]:
                flag = True
                temp = max(temp,nums[ind][1])
                ind +=1
            print(person,temp)

            # print(nums[ind][1])
            if flag:
                ans.append( max(temp,ans[-1]))
            else:
                ans.append(ans[-1])
        
        return sum(ans)
            

        