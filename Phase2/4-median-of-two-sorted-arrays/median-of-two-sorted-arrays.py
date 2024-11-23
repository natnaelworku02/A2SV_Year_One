class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        leng = len(nums1) + len(nums2)

        if leng % 2:
            l = 0
            r = 0

            count = 0

            while l < len(nums1) and r < len(nums2):
                if count == leng //2:
                    # print(count,leng//2)
                    return min(nums1[l],nums2[r])
                
                if nums1[l] > nums2[r]:
                    r += 1
                else:
                    l += 1
                count += 1
            
            while l < len(nums1):
                if count == leng //2:
                    return nums1[l]
                
                l += 1
                count += 1
            
            while r < len(nums2):
                if count == leng //2:
                    return nums2[r]
                
                r += 1
                count += 1
        
        else:
            first = leng//2 -1
            second = leng//2

            l = 0 
            r = 0

            count = 0
            # print(first,second)
            ans = 0
            while l < len(nums1) and r < len(nums2):
                if count == first:
                    # print(count,first,l,r)
                    ans += min(nums1[l],nums2[r])
                    # print(min(nums1[l],nums2[r]))
                if count == second:
                    ans += min(nums1[l],nums2[r])
                    # print(min(nums1[l],nums2[r]))

                    break
                if nums1[l] > nums2[r]:
                    r += 1
                else:
                    l += 1
                count += 1
            else:
                while l < len(nums1):
                    if count == first:
                        ans += nums1[l]
                    if count == second:
                        ans += nums1[l]
                        break
                    
                    l += 1
                    count += 1
                else:
                    while r < len(nums2):
                        if count == first:
                            ans +=nums2[r]
                        if count == second:
                            ans += nums2[r]
                            break
                        
                        r += 1
                        count += 1
                print(ans)
            return ans/2
                

