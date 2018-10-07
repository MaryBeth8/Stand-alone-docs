"""This function takes a list, examines elements from the front of lst until it finds 
an element that is not an even number, then returns the list from that point (inclusive) 
to the end. If every element in lst is even, returns an empty list.
For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) returns [11, 12, 15].
"""

def not_evens(lst):
  new_lst = []
  for item in lst:
    if item % 2 == 0:
      continue
    else:
      new_lst = lst[lst.index(item):]
      break
  return new_lst
  
print(not_evens([4, 8, 10, 11, 12, 15]))
print(not_evens([4, 8, 10]))