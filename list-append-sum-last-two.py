"""This function adds the last two elements of lst together and appends the result to lst. 
It does this process three times and then return lst.
"""

def append_sum(lst):
  new_lst = lst
  count = 3
  while count != 0:
    last1 = new_lst[-1]
    last2 = new_lst[-2]
    new_lst.append(last1 + last2)
    count -= 1
  return new_lst

print(append_sum([1, 1, 2]))