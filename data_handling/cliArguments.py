# run `python cliArguments.py {name} {age}`

import sys

name = sys.argv[1]
age = int(sys.argv[2])

print('% s is a good age, % s' % (age, name))