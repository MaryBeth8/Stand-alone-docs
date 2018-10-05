"""Create a function that has two parameters named lst and index. The function should 
double the value of the element at index of lst and return the new list with the doubled 
value. If index is not a valid index, the function should return the original list.""""

def double_index(lst, index):
  if index <= (len(lst) - 1):
    new_lst = lst
    new_lst[index] = lst[index] * 2
    return new_lst
  else:
    return lst

print(double_index([3, 8, -10, 12], 2))
