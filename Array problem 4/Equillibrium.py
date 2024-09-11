def equi_1(arr):
    leftsidesum=0
    rightsidessum=0
    n=len(arr)
    for i  in range(n):
        leftsidesum=0
        rightsidessum=0
        for j in range(i):
            leftsidesum+=arr[j]
        for j in range(i+1,n):
            rightsidessum+=arr[j]
        if leftsidesum==rightsidessum:
            return i
    return -1
arr=[2,2,1,2,2]       
print(equi_1(arr))