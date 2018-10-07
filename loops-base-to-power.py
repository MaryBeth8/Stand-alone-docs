"""This function takes two lists as parameters named bases and powers. 
It returns a new list containing every number in bases raised to every number in powers.
"""

def exponents(bases, powers):
  results = []
  for base in bases:
    for power in powers:
      results.append(base ** power)
  return results

print(exponents([2, 3, 4], [1, 2, 3]))