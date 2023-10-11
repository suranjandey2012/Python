import time
import random as r


permutation_list=[]

def addpermutation(matrix,m):
    global permutation_list
    l=[]
    for c in range(m):
        for r in range(m):
            if(matrix[r][c]!=0):
                l.append(matrix[r][c])
    permutation_list.append(l)


def generate_permutation(n,inp_list,matrix,occupied,m,limit,start):
    if ((time.time() - start) > limit):
        return
    if(n==0):
        for i in range(m):
            matrix[n][i]=inp_list[n]
            occupied[i]=1
            generate_permutation(n+1,inp_list,matrix,occupied,m,limit,start)
            if ((time.time() - start) > limit):
                return
            occupied[i] = 0
            matrix[n][i] = 0
        return
    elif(n==m-1):
        for i in range(m):
            if ((time.time() - start) > limit):
                return
            if(1!=occupied[i]):
                matrix[n][i]=inp_list[n]
                occupied[i]=1
                addpermutation(matrix,m)
                #print(matrix)
                occupied[i]=0
                matrix[n][i]=0
        return
    else:
        for i in range(m):
            if(1!=occupied[i]):
                matrix[n][i]=inp_list[n]
                occupied[i]=1
                generate_permutation(n+1,inp_list,matrix,occupied,m,limit,start)
                if ((time.time() - start) > limit):
                    return
                occupied[i]=0
                matrix[n][i]=0
        return

def checksorted(array):
    if ((time.time() - start) > limit):
        print("Time Limit Exceeded for size:", len(array))
        return False
    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            return False
    return True


#Taking Input
#inp_list=list(map(int,input("Enter the elements of the array:").split()))
size=1
limit=1200
while(True):
    inp_list=[]
    for i in range(size):
        inp_list.append(r.randint(-100,100))

    start=time.time()

    if(size==1):
        print("Time To sort array of size:", size, "is", (time.time() - start), end=" ")
        print(inp_list)

    matrix=[[0 for i in range(len(inp_list))] for j in range(len(inp_list))]
    occupied=[0 for i in range(len(inp_list))]

    #Generating Permutation using 2D matrix
    generate_permutation(0,inp_list,matrix,occupied,len(inp_list),limit,start)

    if((time.time()-start)>limit):
        print("Time Limit Exceeded for size:",size)
        break
    #print("Generated Permutation list")
    #printing all possible permutation stops when list is sorted
    flag=0
    for array in permutation_list:
      if(checksorted(array) and ((time.time()-start)<=limit)):
        print("Time To sort array of size:",size,"is",(time.time()-start),end=" ")
        print(array)
        break
      elif(((time.time()-start)>limit)):
          print("Time Limit Exceeded for size:", size)
          flag=1
          break
    if(flag):
        break

    permutation_list.clear()

    size+=1


