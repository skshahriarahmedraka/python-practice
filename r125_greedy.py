#furthest you can go with index value
li=list(map(int,input().split(" ")))
further=0
for i in range(len(li)):
    if i>further:
        break
    further=max(further,li[i]+i)
    
    i+=1
print(further)
