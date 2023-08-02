
AList=[1,2,3,6,5,4,3,2,1]

for i in range(len(AList)-1):
    min_index=i
    for j in range(i+1,len(AList)):
        if AList[j]<AList[min_index]:
            min_index=j
    AList[i],AList[min_index]=AList[min_index],AList[i]
print(AList)
print(AList[-2])