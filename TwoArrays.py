def twoArrays(k, A, B):
    A.sort();
    B.sort();
    B.reverse();
    for i in range(len(A)):
        if(A[i]+B[i]<k):
            return("NO");
    return("YES");
