class Solution {
  List<int> twoSum(List<int> nums, int target) {

   Map <int,int> comp = {};

   for (var i = 0; i < nums.length;i ++){
    var diff = target - nums[i];
    if (comp.containsKey(diff)) {
        return [comp[diff]!,i];
    }
    comp[nums[i]] = i;
   }
    return [-1,-1];
  }
}