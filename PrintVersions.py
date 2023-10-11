n=int(input())
lower=list(input().split('.'))
upper=list(input().split('.'))
if(len(lower)<n):
    while(len(lower)!=n):
        lower.append('0')
if(len(upper)<n):
    while(len(upper)!=n):
        upper.append('0')
#print(lower,upper)
lowerstr,upperstr='',''
for i in range(len(lower)):
    lowerstr=lowerstr+lower[i]
for j in range(len(upper)):
    upperstr=upperstr+upper[j]
#print(lowerstr,upperstr)
print("The versions are as follows:")
for k in range(int(lowerstr),int(upperstr)+1):
    '''version=list(str(k))
    #print(version)
    #print(str(version))
    versionprint=""
    for l in range(len(version)):
        versionprint=versionprint+version[l]+'.'
    print(versionprint.rstrip('.'))'''
    print('.'.join(list(str(k))))
    




