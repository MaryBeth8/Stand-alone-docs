"""This function appends all of the numbers between 1 and the size of lst (inclusive) 
to the end of lst, then returns the new list.
"""

def append_size(lst):
  for num in range(1, len(lst) + 1):
    lst.append(num)
  return lst

print(append_size([23, 42, 108]))