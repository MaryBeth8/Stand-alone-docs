"""This function will return the last element of one of two lists that has more elements. 
If both lists are the same size, then it returns the last element of the first list.
"""

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))