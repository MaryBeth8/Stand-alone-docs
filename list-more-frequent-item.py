"""Create a function that returns either item1 or item2 depending on which item appears 
more often in lst. If the two items appear the same number of times, return item1.
"""

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
