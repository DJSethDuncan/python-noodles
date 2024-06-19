import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

  logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')

  try:

    quotient = dividend/divisor  
    print (quotient)

  except Exception as e:

    logging.error(' The exception that occurred is: ' + str(e));

if __name__ == '__main__': 

  dividend = int(5)
  divisor = int(0)
  divideByZeroError(dividend,divisor)