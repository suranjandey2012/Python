'''def function(a, b, c):
    print('Inside 1:', hex(id(a)), hex(id(b)), hex(id(c)))
    b +=2
    print('Inside 2:', hex(id(a)), hex(id(b)), hex(id(c)))
x, y, z = 10, 20, 20
print('Outside:', hex(id(x)), hex(id(y)), hex(id(z)))
function(x, y, z)'''

import math

'''print(math.fsum([1/7]*7))

sum=(1/7)

for i in range(7):
    sum+=(1/7)
    
print(sum)'''
'''
print(math.exp(1/99))
print(math.expm1(1/99))  #-> expm1 has better precision than exp
'''

'''
s1,s2={3,4},{1,2}
s3=set()
for i in s1:
    for j in s2:
        s3.add((i,j))
        print(s3)
        i+=1
        j+=1
print(s3)'''

import numpy as np

print(np.random.randint(1,100))