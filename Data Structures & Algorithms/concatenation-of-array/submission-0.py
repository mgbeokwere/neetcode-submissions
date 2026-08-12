class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []
        nums_length = len(nums)

        for i in range(2 * nums_length):
            # make sure index is in range 
            j = i % nums_length
            new_arr.append(nums[j])    

        return new_arr 