def linear_search (numbers, key):
  for i in numbers:
    if i == key:
      return i
    
  return -1