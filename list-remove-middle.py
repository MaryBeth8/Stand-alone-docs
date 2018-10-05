"""Create a function that returns a list where 
All elements in lst with an index between start and end (inclusive) have been removed.
"""

def remove_middle(lst, start, end):
  first_half = lst[:start]
  second_half = lst[end + 1:]
  return first_half + second_half 

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))