"""Create a function that returns True if item appears in lst more than n times, 
otherwise return False.
"""

def more_than_n(lst, item, n):
  return lst.count(item) > n
    

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 2))