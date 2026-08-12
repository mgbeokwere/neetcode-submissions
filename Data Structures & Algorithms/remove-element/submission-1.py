class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count the number of values that are not eqaul to k
        k = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[k] = nums[index]
                k +=1

        return k

        

        