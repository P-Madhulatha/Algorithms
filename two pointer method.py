def two_pointer(arr,t):
    i,j=0,len(arr)-1
    s=0
    while i<=j:
        s=arr[i]+arr[j]
        if s==t:
            return 'YEAH WE FOUND IT'
        elif s>t:
            j-=1
        else:
            i+=1
    else:
        return 'OH! WE NOT FOUND IT'
            
arr=list(map(int,input().split()))
t=int(input())
print(two_pointer(arr,t))
