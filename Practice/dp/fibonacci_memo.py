def Fib_mem(n, memo):
    if memo[n] != None:
        return memo[n]
    
    if n<=1:
        result = n
    
    else:
        result = Fib_mem(n-1, memo) + Fib_mem(n-2, memo)
    
    memo[n] = result
    return result


def fib_bottom_up(n,memo):
    if n<=1:
        result = n
        memo[n] = result
    else:
        result = Fib_mem(n-1, memo) + Fib_mem(n-2, memo)
        memo[n] = result
    
    return memo
    
if __name__ == "__main__":
    n = int(input("Enter number: "))
    memo = [None]*(n+1)
    
    fib_series = [Fib_mem(i, memo) for i in range(n+1)]
    
    print(f"Fib series: {fib_series}")
    
    memo = [None]*(n+1)
    result = fib_bottom_up(n, memo)
    
    print(result)