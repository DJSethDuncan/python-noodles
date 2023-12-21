# Recursion is irritating but doing the fibonacci thing is a good example

def fibonacci(v1, v2, run_cnt):
  print('% s + % s = % s' % (v1, v2, (v1 + v2)))

  if run_cnt <= 1:                    # base case -- we ran for the user-specified count
    pass                              # do nothing
  else:                               # recursive case
    fibonacci(v2, v1+v2, run_cnt-1)   # fib

print ('Fibonacci, yo')

run_for = int(input('How many steps you want, bro? '))

fibonacci(0, 1, run_for)


