"""This function sums the elements of the list until the sum is greater than 9000. 
When this happens, the function returns the sum. If the sum of all of the elements is 
never greater than 9000, the function returns the total sum of all the elements. 
If the list is empty, the function returns 0.
"""

def over_nine_thousand(lst):
  sum = 0
  for item in lst:
    if sum < 9000:
      sum += item
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
