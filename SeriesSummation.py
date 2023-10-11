#1/1 + 11/12 + 111/123 + · · · + 111 . . . n times/123 . . . n

import math

n=int(input())
numerator,denominator=0,''
sumlist=[]
for i in range(n):
    numerator=numerator*10+1
    denominator=denominator+str(i+1)
    #print(numerator, int(denominator))
    sumlist.append(numerator/int(denominator))
print(math.fsum(sumlist))
