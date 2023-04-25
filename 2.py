def is_fibonacci(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    else:
        a = 0
        b = 1
        while b < n:
            c = a + b
            a = b
            b = c
        if b == n:
            return True
        else:
            return False
        
print(is_fibonacci(6))