# Usage
# argv1 - The number of strings you want to generate
# argv2 - The length of strings that will be generated
import string
import random
import sys

chars = string.letters + string.digits

numStrings = sys.argv[1]
sizeString = int(sys.argv[2])
if sizeString < 5:
    sizeString = 5

# Alphanumeric +
chars = string.letters + string.digits + string.punctuation

for num in xrange(int(numStrings)):
    print ''.join((random.choice(chars)) for x in range(random.randint(5,int(sizeString))))
