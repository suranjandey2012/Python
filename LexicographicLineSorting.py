
def partition(line,s,e):
    #print(line,s,e)
    pivot=line[s]
    i,j=s,s+1
    while(j<=e):
        if(line[j].lower()<=pivot.lower()):
            i+=1
            temp=line[i]
            line[i]=line[j]
            line[j]=temp
        j+=1
    line[s]=line[i]
    line[i]=pivot
    return i


def sort(line,s,e):
    #print(line)
    if(len(line)<=1 or s>=e):
        return
    j=partition(line,s,e)
    sort(line,j+1,e)
    sort(line,s,j-1)



def printlexic(filename):
    fread=open(filename,"r")
    lines=fread.readlines()
    fread.close()
    fwrite=open(filename,"w")
    counter=0
    for line in lines:
        counter+=1
        line=line.split()
        if(line[-1]=='\n'):
            line=line[:-1]
        sort(line,0,len(line)-1)
        if(counter!=len(lines)):
            line.append("\n")
        fwrite.write(" ".join(line))
    fwrite.close()
    
printlexic("Input.txt")












