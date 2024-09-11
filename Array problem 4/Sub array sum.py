def sub_arr(arr,n,sum):
    for i in range(n):
        currentsum=arr[i]
        j=i+1
        while j <= n:
            if currentsum==sum:
                print("Sum found between ",i,j-1)
                return 1
            if currentsum>sum or j==n:
                break
            currentsum=currentsum+arr[j]
            j+=1
    print("Not found") 
    return 0
arr=[9,4,3,8,1]
n=len(arr)
sum=25
sub_arr(arr,n,sum)
