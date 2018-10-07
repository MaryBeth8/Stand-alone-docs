"""Adds the string 'Hello, ' in front of each name in names and appends the 
greeting to the list. Returns the new list containing the greetings.
"""

#version1

def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append('Hello, ' + name)
  return greetings
  
print(add_greetings(["Owen", "Max", "Sophie"]))

#returns a list of greetings [...]


#version2

def add_greetings(names):
  greetings = []
  greetings.append(['Hello, ' + name for name in names])
  return greetings

#returns a list of greetings inside the list greetings [[...]]