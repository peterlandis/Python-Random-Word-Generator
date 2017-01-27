# Usage
# argv1 - The number of words you want to generate from the unix dictonary

import string
import random
import sys
import commands

numWords = int(sys.argv[1])
count=0
dictSizeArr = commands.getstatusoutput("wc -l /usr/share/dict/words | cut -f3 -d' '")
dictSize = int(dictSizeArr[1])

dictArray = []

# Load the dictonary into an array
with open("/usr/share/dict/words", "r")as ins:
    for line in ins:
        wordLine=line.split("\n");
        dictArray.append(wordLine[0])

#Loop based on the number of words and randomly select words from the dictonary
for num in range(numWords):
    ranNum = random.randint(1,dictSize-1)
    print(dictArray[ranNum])
