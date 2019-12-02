def minimumSwaps(arr):
    sum=0
    indexes={}
    for i in range(len(arr)):
        indexes.update({arr[i]:i})

    for i in range(len(arr)):
        if not arr[i]==i+1:
            #arr[i]=valor actual
            #indexes[i+1]=indice donde esta el valor correcto
            temp=arr[i]
            arr[i],arr[indexes[i+1]]=arr[indexes[i+1]],arr[i]
            indexes.update({temp:indexes[i+1]})
            indexes.update({i+1:i})
            sum+=1
    return sum
