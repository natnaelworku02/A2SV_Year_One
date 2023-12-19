class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        arr=[char for char in s]
        while i<len(arr):
            leng=len(arr[i:])
            if leng>=2*k:
                print(arr[i+k-1:i:-1])
                arr[i:i+k]=arr[i:i+k][::-1]
                i+=2*k


            elif leng<2*k and leng>=k:
                arr[i:i+k]=arr[i:i+k] [::-1]
                break
            elif leng<k:
                arr[i:i+leng]=arr[i:i+leng][::-1]
                break
        return ''.join(arr)