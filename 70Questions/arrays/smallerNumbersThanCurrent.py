def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    temp =  sorted((nums)) # sort the array which we iterating
    d = {} # create a new dict to hold these changing variables

    for i, num in enumerate(temp): # iterate through the array
        if num not in d: # if not in d
            d[num] = i

    returned = []
    for i in nums:
        returned.append(d[i]) # append into returned the index
    return returned
