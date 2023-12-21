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

numbers = [2, 3, 5, 8, 11, 25, 37, 42, 57]
print('Numbers:', end=' ')

for num in numbers:
  print(num, end=' ')
print()

key = int(input('Enter a value: '))
key_index = binary_search(numbers, key)

if key_index == -1:
  print('% s was not found.' % key)
else:
  print('Found % s at index % s' % (key, key_index))