#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures.
def unqiue_string(string):
  chars={}
  for s in string:
    if s in chars:
      return False
    chars[s]=1
  return True

#2nd WAY
def unique_string(string):
  unique=set()
  for s in string:
    if s in unique:
      return False
    unique.add(s)
  return True
# Time Complexity: O(N)
