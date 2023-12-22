# generate a bigass array
# note: this takes like, some time to generate
# since we're generating 10 million numbers

# EXAMPLE RESULT:
# Number array generated with 10000000 numbers.
# What number do you want to find? 9999997
# Sort completed in 3083.804084 ms 
# Linear search completed in 1276.310782 ms 
# Binary search completed in 0.0147 ms 

import random
import time

iterations = 10000000
iteration = 0
numberArray = []

def linear_search (numbers, key):
  for i in numbers:
    if i == key:
      return i
    
  return -1

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
  return -1 #not found

while iteration < iterations:
  numberArray.append(random.randint(1, iterations))
  iteration += 1

sortStartTime = time.perf_counter_ns()
numberArray.sort()
sortEndTime = time.perf_counter_ns()

print('Number array generated with % s numbers.' % iterations)
find = int(input('What number do you want to find? '))

linearStartTime = time.perf_counter_ns()
linear_search(numberArray, find)
linearEndTime = time.perf_counter_ns()

binaryStartTime = time.perf_counter_ns()
binary_search(numberArray, find)
binaryEndTime = time.perf_counter_ns()

elapsedSortTime = (sortEndTime - sortStartTime) / 1000000
elapsedLinearTime = (linearEndTime - linearStartTime) / 1000000
elapsedBinaryTime = (binaryEndTime - binaryStartTime) / 1000000

print('Sort completed in % s ms ' % elapsedSortTime)
print('Linear search completed in % s ms ' % elapsedLinearTime)
print('Binary search completed in % s ms ' % elapsedBinaryTime)
