"""This function takes a list of numbers named nums as a parameter.
It returns the amount of numbers in that list that are divisible by 10.
"""

def divisible_by_ten(nums):
  divisible = [num for num in nums if num % 10 == 0]
  return len(divisible)
  
print(divisible_by_ten([20, 25, 30, 35, 40]))