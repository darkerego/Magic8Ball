#!/usr/bin/env python3.6
# Python3 Powered Magic 8Ball

"""  This program is cooler than your typical random magic 8ball because it determines the answer by first calculating the md5sum of the question 
and then converting the hash into binary. Next, each numeral in the binary is added together to form the final sum. If the sum %2 == 0 , then return 
an affirmative answer, otherwise return a negative  """

import random,hashlib,binascii

print("""
       _.a$$$$$a._
     ,$$$$$$$$$$$$$.
   ,$$$$$$$$$$$$$$$$$.
  d$$$$$$$$$$$$$$$$$$$b
 d$$$$$$$$~'"`~$$$$$$$$b
($$$$$$$p   _   q$$$$$$$)
$$$$$$$$   (_)   $$$$$$$$
$$$$$$$$   (_)   $$$$$$$$
($$$$$$$b       d$$$$$$$)
 q$$$$$$$$a._.a$$$$$$$$p
  q$$$$$$$$$$$$$$$$$$$p
   `$$$$$$$$$$$$$$$$$'
     `$$$$$$$$$$$$$'
       `~$$$$$$$~'
""")


       
# return a random yes or no answer from the following dictionaries
def verboseMaybe(side):
    yRan = ['Yes, absolutely!', 'You already know the answer is yes', 'Affirmative!','Probably.','I would say so.', 'Maybe...', 'Most likely.']
    nRan = ['No, certaintly not!','Not today...','No, definitely not', 'Maybe , maybe not...', 'Ask me later','I dont think so', 'Dubious.']
    if side == 'yes':
        random.shuffle(yRan)
        return(yRan[0])
    if side == 'no':
       random.shuffle(nRan)
       return(nRan[0])

# If final sum of binary is divisable for 0, return true (yes); else return false (no)
def maybe(magic):
    if magic %2 == 0:
        return True
    else:
        return False


# calculate the md5 hash of question, than convert the hash into binary, add each binary digit together, return sum
def convertToBinary(data):
    hash_object = hashlib.md5(data.encode())
    hashed=(hash_object.hexdigest())
    toBin = bin(int.from_bytes(data.encode(), 'big'))
    ret = sum(int(x) for x in toBin if x.isdecimal())
    return(ret)



# Start - Ask user their question
data=input("Ask me a yes or no question >> ")
_bin = convertToBinary(data)
res = maybe(_bin)

if res:
    answer = verboseMaybe('yes')
else:
    answer = verboseMaybe('no')

print(answer)
