import numpy as np

def Isunique(l):
    for i in range(N):
        if(l.count(l[i])>1 or l[i]>9 or l[i]<1):
            return False
    #print(l)
    return True



def Issudoku(matrix):
    #Row And Column Level Check
    for i in range(N):
        if(not Isunique(list(np.array(matrix)[i,:]))):
            return False
        if(not Isunique(list(np.array(matrix)[:,i]))):
            return False
        
    #submatrix Level Check
    (rstart,rend)=(0,3)
    while(rend<=N):
        (cstart,cend)=(0,3)
        while(cend<=N):
            if(not Isunique(list(np.array(matrix)[rstart:rend,cstart:cend].flatten()))):
                return False
            cstart=cend
            cend+=3
        rstart=rend
        rend+=3 
    return True

N=9
matrix=[list(map(int,input().split())) for j in range(N)]
#print(mat)
if(not Issudoku(matrix)):
    print("Invalid")
else:
    print("Valid")    