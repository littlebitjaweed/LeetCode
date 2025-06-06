class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix= [0]*len(nums)
        self.prefix[0]=nums[0]
        for i in range(1,len(nums)):
            self.prefix[i]=self.prefix[i-1]+nums[i]
            
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            sum= self.prefix[right]
        else:
            sum = self.prefix[right]-self.prefix[left-1]
        return sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)