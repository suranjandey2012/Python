def printeven(lines,value):
    for i in range(lines//2):
        k=lines//2
        for j in range(i+1):
            print(k,end=" ")
            k-=1
        repeat=k+1
        for r in range(lines-2*(i+1)):
            print(repeat,end=" ")
        for r in range(i+1):
            print(repeat,end=" ")
            repeat+=1
        print()
    for i in range(lines//2):
        p=value
        for j in range(lines//2-i):
            print(p,end=" ")
            p-=1
        p+=1
        for j in range(2*i):
            print(p,end=" ")
        for j in range(lines//2-i):
            print(p,end=" ")
            p+=1
        print()    



def printodd(lines,value):
    for i in range(lines//2+1):
        k=value
        for j in range(i+1):
            print(k,end=" ")
            k-=1
        k+=1    
        repeat=lines-(i+1)*2    
        for r in range(repeat):
            print(k,end=" ")
        if(k==1):
            m=k+1
        else:
            m=k    
        while(m<=value):
            print(m,end=" ")
            m+=1
        print()
    for i in range(lines//2):
        m=value
        for j in range(lines//2-i):
            print(m,end=" ")
            m-=1
        m+=1    
        for j in range(2*i+1):
            print(m,end=" ")
        for j in range(lines//2-i):
            print(m,end=" ")
            m+=1
        print()                    


#main block
lines=int(input())
if(lines%2==0):
    value=lines//2
    printeven(lines,value)
else:
    value=(lines//2)+1
    printodd(lines,value)   






    







    



