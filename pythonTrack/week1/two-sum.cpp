class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       
       vector <int> num;
       int diff;
       unordered_map<int, int> m;
       for(int i=0;i<nums.size();i++){
            diff=target-nums[i];
            if(m.find(diff)!=m.end())
       return {m[diff],i};
   m[nums[i]] = i;

       }
    //     for(int i=0;i<nums.size();i++){
    //         for(int j=i+1;j<nums.size();j++){
    //         if((nums[i]+nums[j])==target){
    //    num.push_back(i);
    //     num.push_back(j);
    //      return num;}
         
    //     }
    //     }
    return num;
    }
};