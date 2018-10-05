"""This function returns a list of every third number between a number 'start' and 
100 (inclusive). If start is greater than 100, the function returns an empty list.
"""

def every_three_nums(start):
  nums = []
  if start <= 100:
    for n in range(start, 100 + 1, 3):
      nums.append(n)
  return nums

print(every_three_nums(81))