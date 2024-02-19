class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre  = [0]*n
        rev_pre = [0]*n
        arr = [0] *n
        sorted_index = defaultdict(list)
        for i in range(n):
            sorted_index[nums[i]].append(i)
        for key , value in sorted_index.items():
            if len(value) == 1:
                arr[value[0]] = 0
            else:
                count = 0
                rev_count = 0
                vlen = len(value)
                for i in range(len(value)):
                    if i == 0:
                        pre[value[i]] = 0
                    else:
                        pre[value[i]] = (value[i] - value[i-1])*count + pre[value[i-1]]
                    count +=1
                    if vlen-i-1 == len(value) -1:
                        rev_pre[value[vlen-i-1]] = 0
                    else:
                        rev_pre[value[vlen - i -1]] = (value[vlen -i] - value[vlen - i -1]) *rev_count + rev_pre[value[vlen -i]]
                        # print(value[vlen -i],value[vlen -i - 1],rev_count,[value[vlen -i]])
                    rev_count += 1
                # print(pre,rev_pre)
                for i in range(len(value)):
                    arr[value[i]] = pre[value[i]] +rev_pre[value[i]]



        # for i in range(n):
        #     pre[i] += 
        #     rev_pre[nums[-1-i]] += n-1-i
        # arr = [0]*len(nums)
        # for i in range(len(nums)):

        #     pre[nums[i]] -= i
        #     arr[i] = pre[nums[i]]
        # for i in range(len(nums)-1,-1,-1):
        #     rev_pre[nums[i]] -= i
        #     arr[i] = max(arr[i],rev_pre[nums[i]])
        return arr