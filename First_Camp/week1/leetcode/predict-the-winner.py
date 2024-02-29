class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def game(left,right):
            if left == right:
                return nums[left]
            left_choice  = nums[left] - game(left + 1, right)
            right_choice = nums[right] - game(left,right - 1)
            return max(left_choice,right_choice)
        return game(0,len(nums) - 1) >= 0
        