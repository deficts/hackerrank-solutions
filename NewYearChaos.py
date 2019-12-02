def minimumBribes(q):
    sum=0
    for i in range(len(q)-1,0,-1):
        if(q[i]<i+1):
            if(q[i-1]==i+1):
                sum+=1
                q[i],q[i-1]=q[i-1],q[i]
            elif(q[i-2]==i+1):
                sum+=2
                q[i-1],q[i-2]=q[i-2],q[i-1]
                q[i],q[i-1]=q[i-1],q[i]
            else:
                print('Too chaotic')
                return
    print (sum)
