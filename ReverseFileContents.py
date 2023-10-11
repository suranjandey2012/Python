
def insertrev(filename):
    fread=open("Input.txt","r")
    line=fread.readline()
    reversed=[]
    while(line!=""):
        for words in line.split():
            reversed.append(words[::-1])
            reversed.append(" ")
        #print(reversed)
        reversed=reversed[:len(reversed)-1] 
        reversed.append('\n')
        line=fread.readline()
    fwrite=open("Input.txt","w")
    fwrite.writelines(reversed)
    fread.close()
    fwrite.close()


insertrev("Input.txt")