class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      range_set=set(range(left,right+1))
      super_set=set()
      for value in ranges:
        one,two=value
        super_set.update(range(one,two+1))
      if super_set>=range_set:
        return True
      else:
        return False
        
                
        
        