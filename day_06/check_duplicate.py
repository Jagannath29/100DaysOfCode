
# In the problem of checking duplicate values, you will be given an array of integers. You need to check if any value appears more than once. Below is an example of the input and output of this problem:

# Input: [3,1,3,8]
# Output: True

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    else:
        return False

nums = [3,1,3,8]
print(containsDuplicate(nums))