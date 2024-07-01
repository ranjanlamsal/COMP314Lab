def string_matching(t, p):
    n = len(t)
    m = len(p)
    
    # print(f"n: {n}, m: {m}")
    
    for i in range(0, n-m+1):
        j = 0
        print(f"{p[j], t[i+j]} ")
        while j < m and p[j] == t[i+j]:
            print(f"{p[j], t[i+j]} ")
            j = j+1
        
        if j == m :
            return i
    
    return -1

if __name__ == "__main__":
    
    t = "Student"
    p = "dent"
    print(f"original text: {t}")
    print(f"string to match: {p}")
    
    key = string_matching(t, p)
    
    print(f"Search key: {key}")
    