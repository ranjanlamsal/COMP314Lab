def activity_recursive(s, f, k, n):
    m = k+1
    
    while m < n and s[m] < f[k]:
        m += 1
    
    if m < n:
        return f', a{m} ' + activity_recursive(s, f, m, n)
    
    return ''

def activity_iterative(s, f):
    n = len(s)
    A = 'a0'
    k = 0
    for m in range(1,n):
        if s[m] >= f[k]:
            A = A + f', a{m}'
            k = m
    return A
    
        

if __name__ == "__main__":
    
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12 ]
    f = [4, 5, 6, 7, 9, 9 , 10 , 11, 12, 14, 16]
    
    activities = activity_recursive(s, f, 0, 11)
    act = activity_iterative(s, f)
    
    print('a0'+activities)
    print(act)