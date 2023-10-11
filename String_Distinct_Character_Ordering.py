def Getdistinctletters(word):
    newword=""
    for letter in word:
        if letter not in newword:
            newword=newword+letter
    return newword


words=input().split()

lastword=Getdistinctletters(words[-1].lower())
#print(lastword)
flag=True
for w in words[:len(words)-1]:
    i,j=0,0
    check=w.lower()
    while(i<len(check)):
        if(check[i]==lastword[j]):
            None
        elif((check[i]!=lastword[j]) and (check[i] in lastword[j+1:])):
            j=lastword.index(check[i])
        elif((check[i]!=lastword[j]) and (check[i] in lastword[:j])):
            flag=False
            break
        i+=1
    if(not flag):
        print("Order not Preserved")
        break
if(flag):
    print("Order is preserved")        

              


