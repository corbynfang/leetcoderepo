# We define a harmonious array as an array where the difference between its maximum value and its minmum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence its possible subsequences.
# Ex:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: the longest harmonious subsequence is [3,2,2,2,3]
# Intution: A harmonious sequence is defined as a sequence where the different between the maximum and minimum numbers is exactly 1! The goal is to find the length of the longest such subsequence in the given array.


# Sliding Window Technique using i,j pointers

def findLHS(self, nums: List[int]) -> int:
    nums.sort()
    j = 0
    maxLength = 0

    for i in rangle(len(nums)):
        while nums[i] - nums[j] > 1:
            j += 1
        if nums[i] - nums[j] == 1:
            maxLength = max(maxLength, i - j + 1)
    return maxLength

# Hash Map
# Use a Hash Map to count how many times each number appears in the array.
# Check valid pairs for each number num in the map check if num + 1 also exists in the map. If yes, the pair (num, num + 1) forms a valid harmonious subsequence. Calculate the length of this subsequence (count[num] + count[num + 1])

def findLHS(self, nums: List[int]) -> int:
    frequency_map = Counter(nums) # Frequency of the counting of each number
    maxLength = 0

    for num in frequency_map:
        if num + 1 in frequency_map:
            currentLength = frequency_map[num] + frequency_map[num + 1]
            maxLength = max(maxLength, currentLength)
    return maxLength
