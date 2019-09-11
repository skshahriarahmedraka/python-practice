max=100000
def power(x,n):
    arr=[0 for i in range(max)]
    if (n<=0 and x<=0 )or x==0:
        print("invalid")
        return
	if (n == 0) : 
	    print("1") 
	    return
    tem=x
    size=0
    while tem>0:
        arr[size]=tem%10
        tem=tem//10
        size+=1
    for i in range(2,n+1):
        carry=0
        for j in range(size):
            ex=arr[j]*x+carry
            arr[j]=ex%10
            carry=ex//10
        while carry:
            arr[size]=carry%10
            carry=carry//10
            size+=1
    for i in range(size-1,-1,-1):
        print(arr[i],end="")
    
b,n=list(map(int,input().split(" ")))
power(b,n)