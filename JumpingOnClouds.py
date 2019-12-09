def jumpingOnClouds(c):
    n=len(c)
    j=0
    i=0
    while i < n:
        print(i)
        if i+2<n :
            if(c[i+2]==0):
                j+=1
                i+=1
            elif(c[i+1]==0):
                j+=1
        elif i+1<n:
            if(c[i+1]==0):
                j+=1
        i+=1
    return j
