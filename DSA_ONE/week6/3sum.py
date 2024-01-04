class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the  numbers  to allow usage of two pointers concept
        nums.sort()
        di = []
        ans=[]
        for i in range(len(nums)):
            ''' condition to check if the current value is same as prev
             because if itis the same we already found an
            answer if there exists one for the previous '''
            if i >0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 
            k = len(nums) - 1
            '''
            basic two pointer iteration
            '''
            while j < k:
                add = nums[i] + nums [j] + nums [k]
                if add == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                elif add > 0:
                    k-=1
                else:
                    j+=1
                


        return ans

        