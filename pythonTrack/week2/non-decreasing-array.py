class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        #  loop through the elements 
        for index in range(len(nums)-1):
            ''' check if the first value is greater than second value
             since we can't minus in index 0 '''
            if index==0 and nums[index]>nums[index+1]:
                #update count
                count+=1
            # check if index is not 2 then if previous value is gerater than next
            elif index>0 and nums[index]>nums[index+1]:
                '''check if the next value and the previous one compared to index
                  is small then update its value to the value of the index as
                  it is the recent max '''
                if nums[index+1]<nums[index-1]:
                    nums[index+1]=nums[index]
                    count+=1
                #  else just change the index value 
                else:
                    
                    nums[index]= nums[index+1]
                    count+=1
                #  check if count excceds
                if count>1:
                    return False

        return True
        