"""Create a function called middle_element that has one parameter named lst.
If there are an odd number of elements in lst, the function will return the middle element.
If there are an even number of elements, the function will return the average of the middle 
two elements.
"""

def middle_element(lst):
  mid = int(len(lst) / 2)
  if len(lst) % 2 == 0:
    return (lst[mid] + lst[mid-1]) / 2
  else:
    return lst[mid]

print(middle_element([5, 2, -10, -4, 4, 5]))