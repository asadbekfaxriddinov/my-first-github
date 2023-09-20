class Solution(object):
    def areNumbersAscending(self, s):
        count = 0
        nums = list()
        s = s.split()
        for i in s:
            if i.isdigit():
                nums.append(int(i))
                
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                return False
                
        for i in nums:
            if nums[0] == i:
                count+=1
        if count == len(nums):
            return False
        
        print(sorted(nums))
        print(nums)
                        
        if nums == sorted(nums):
            return True
        return False
        
a1 = Solution()

a1.areNumbersAscending("46 sad 47 48 dig 49 50 green 51 train 52 broad 53")
