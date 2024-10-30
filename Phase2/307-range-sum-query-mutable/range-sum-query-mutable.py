class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)

        self.build(0,0,self.n - 1)
    
    def build(self,node,nleft,nright):

        if nleft == nright:
            self.tree[node] = self.nums[nleft]
            return
        
        nmid = (nleft + nright)//2
        left_child,right_child = self.findChildren(node)

        self.build(left_child,nleft,nmid)
        self.build(right_child,nmid + 1,nright)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]
        

    def update(self, index: int, val: int) -> None:
        return self.updateval(0,0,self.n - 1,index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0,0,self.n - 1,left,right)
    
    def query(self,node,nleft,nright,qleft,qright):

        if qleft > qright:
            return 0
        
        if qleft== nleft and  nright == qright:
            return self.tree[node]
        
        left_child,right_child = self.findChildren(node)

        nmid = (nleft + nright)//2
        leftval = self.query(left_child,nleft,nmid,qleft,min(qright,nmid))
        rightval = self.query(right_child,nmid + 1,nright,max(qleft,nmid + 1),qright)

        return leftval + rightval


    
    def findChildren(self,node):
        left_child = node*2 + 1
        right_child = node*2 + 2
        return left_child,right_child
    
    def updateval(self,node,nleft,nright,index,val):

        if nleft == nright:
            self.nums[index] = val
            self.tree[node] = val
            return 
        
        nmid = (nleft + nright)//2

        left_child,right_child = self.findChildren(node)
        if index <= nmid:
            self.updateval(left_child,nleft,nmid,index,val)
        else:
            self.updateval(right_child,nmid + 1,nright,index,val)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)