"""This function named takes a list of numbers named nums as a parameter.
It returns the largest number in nums.
"""

def max_num(nums):
  largest = nums[0]
  for num in nums:
    if largest < num:
      largest = num
  return largest

print(max_num([50, -10, 0, 75, 20]))