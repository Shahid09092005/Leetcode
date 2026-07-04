class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        currSum=0
        lst = []
        for i in range(len(nums)):
            if(freq.get(target-nums[i]) is None):
                freq[nums[i]]=i
            else:
                lst.append(freq.get(target-nums[i]))
                lst.insert(1,i)
        return lst
                
