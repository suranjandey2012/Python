N=int(input())
i,j=0,N-1
for l in range(N):
    for k in range(N):
        if((k==i or k==j)):
            print("*",end="")
            #print(k,end="")        
        else:
            print(" ",end="")    

    i+=1
    j-=1
    print()





