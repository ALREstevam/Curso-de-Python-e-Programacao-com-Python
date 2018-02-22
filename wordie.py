"""Random Text Writer"""

import string
from random import randint, choice

vowels = "aeiou"
noRepeatableConsonants = "bcdfghjklmnpqrstvwxyz"
repeatableConsonants = "rsp"
repeatQuantity = 2
specialCharacters = "ç"
punctuation = ".!?;,"
commonPrefixes = ["an", "en"]
commonPostfixes = ["ndo", "ei"]

randomSeed = 3

mininumWordSize = 2
maximumWordSize = 10
avgWordSize = 6


bigWordProbab = 0.5
prefixProbab = 0.5
postfixProbab = 0.5

#---------------------------------------#

random.seed(randomSeed)


if not (mininumWordSize < avgWordSize < maximumWordSize):
    print("Error on word size.")
    input()
    exit()




class WordFingerPrint:
    def UnicodeError
    
    def generateWordFingerprint():
        wordFingerprint = {bigWord: False, hasPrefix: False, hasPostFix: False}
        if random.randint(0, int(10 - int(bigWordProbab * 10)) == 0: #is a big word
            wordFingerprint[bigWord] = True
        if random.randint(0, int(10 - int(prefixProbab * 10)) == 0: #has a prefix
            wordFingerprint[hasPrefix] = True
        if random.randint(0, int(10 - int(postfixProbab * 10)) == 0: #has a postfix
            wordFingerprint[hasPostFix] = True



                      







