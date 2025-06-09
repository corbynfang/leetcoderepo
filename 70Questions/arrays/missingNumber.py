# Missing Number
# Problem: Check the list for the missing number in range(0,n)
# Soultion: O(n): itereate the list and sum(twice: once we are given list and once for expected using range)
# Notes:
#   len() = 0(1)
#   Range object cretion = 0(1)
#   Sum = O(N)
#   +1 in range(n) because it will be excluded otherwise
#

# Sort nums and iterate through the list with i,v. If i does not equal v then return v-1
def missingNumber(self, nums: List[int]) -> int:
    nums.sort()
    for i,v in enumerate(nums):
        if(i != v):
            return v - 1
        if v == len(nums)-1:
            return v+1
