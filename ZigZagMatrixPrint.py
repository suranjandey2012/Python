import random as r

def PrintZigZag(matrix,rs,re,cs,ce):
    if((re-rs)==1 or (ce-cs)==1):
        print(matrix[rs][cs],end=" ")
        return
    midr=(re+rs)//2
    midc=(ce+cs)//2
    #print(rs,re,cs,ce)
    PrintZigZag(matrix,rs,midr,cs,midc)
    PrintZigZag(matrix,rs,midr,midc,ce)
    PrintZigZag(matrix,midr,re,cs,midc)
    PrintZigZag(matrix,midr,re,midc,ce)
    

matrix=[[r.randint(1,8) for i in range(8)] for j in range(16)]
print("Original Matrix")
for i in range(8):
    for j in range(8):
        print(matrix[i][j],end=" ")
    print()    
print("ZigZag MAtrix") 
print(PrintZigZag(matrix,0,8,0,8))