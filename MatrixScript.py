def decodeMatrix(matrix):
    s=''
    c=0
    for j in range(len(matrix[c])):
        for i in range(len(matrix)):
            s+=matrix[i][j]
        c+=1
    s=re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',s)
    print(s)
