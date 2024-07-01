def lcs_recursion(X, Y, m, n):
    if m == len(X) or n ==len(Y):
        return 0
    
    elif X[m] == Y[n]:
        return 1 + lcs_recursion(X,Y, m+1, n+1)
    
    else:
        return max(lcs_recursion(X, Y, m+1, n), lcs_recursion(X,Y,m, n+1))
    
def lcs_BU(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    
    arr = [[0 for i in range(n)] for j in range(m)]
# created a n*m martix
    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]:
                arr[i][j] = 1+ arr[i-1][j-1]
            
            else:
                arr[i][j] = max( arr[i-1][j], arr[i][j-1] )
        
    return arr[m-1][n-1]
                
if __name__ == "__main__":
    X = input("Enter string X:")
    Y = input("Enter string Y:")
    
    max_lcs_recursive = lcs_recursion(X, Y, 0, 0)
    max1 = lcs_BU(X, Y)
    
    
    print(max_lcs_recursive)
    print(max1)
    