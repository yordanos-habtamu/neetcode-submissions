class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        mul=1
        for i in range (0,len(nums)):
            for j in range(0,len(nums)):
                if (i == j):
                    continue
                else:
                    mul *=  nums[j]    
            prod.append(mul)
            mul=1
        return prod


            
        
