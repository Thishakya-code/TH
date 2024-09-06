def kad(a):
    max=-99999999999
    c_max=0
    size=len(a)
    for i in range(0,size):
        c_max+=a[i]
        if max<c_max:
            max=c_max
        if c_max<0:
            c_max=0
    return c_max

def circular(a):
    max_previous=kad(a)
    max_rap=0
    for i in range(0,len(a)):
        max_rap+=a[i]
        a[i]=-a[i]
    max_rap=max_rap+kad(a)
    if max_rap>max_previous:
       return   max_rap
    else:
        return  max_previous
a=[4,5,-7]
print(circular(a))    
        
