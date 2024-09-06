def kad(a,size):
    max=-99999999999
    c_max=0
    for i in range(0,size):
        c_max+=a[i]
        if max<c_max:
            max=c_max
        if c_max<0:
            c_max=0
    return c_max
a=[4,3,-5]            
print(kad(a,len(a)))