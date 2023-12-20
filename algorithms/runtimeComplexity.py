# -----------------------------------------------
# O(1) - Constant
def find_min(x, y):
   if x < y:
      return x
   else:
      return y

# -----------------------------------------------
# O(log N) - Logarithmic
def binary_search(numbers, key):
   low = 0
   high = len(numbers) - 1
   
   while high >= low:
      mid = (high + low) // 2
      if numbers[mid] < key:
         low = mid + 1
      elif numbers[mid] > key:
         high = mid - 1
      else:
         return mid
   return -1  # not found

# O(N) - Linear
# -----------------------------------------------
def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
             return i
    return -1  # not found

# -----------------------------------------------
# O(N log N) - Log-linear
def merge_sort(numbers, i, k):
   if i < k:
      j = (i + k) // 2              # Find midpoint 
      merge_sort(numbers, i, j)     # Sort left part
      merge_sort(numbers, j + 1, k) # Sort right part
      merge(numbers, i, j, k)       # Merge parts

# -----------------------------------------------
# O(N^2) - Quadratic
def selection_sort(numbers):
    for i in range(len(numbers)):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
            
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp

# -----------------------------------------------
# O(c^N) - Exponential
def fibonacci(N):
    if (1 == N) or (2 == N):
        return N
    return fibonacci(N-1) + fibonacci(N-2)