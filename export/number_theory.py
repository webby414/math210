def is_prime(a):
    if a<=1:
        return False
    for div in range(2,a):
        if a % div == 0:
            return False
    return True
    
def rep_as_squares(N):
    """Find all representations of N as a sum of squares a**2 + b**2 = N."""
    reps = []
    for a in range(1,N):
        for b in range(a,N):
            if a**2 + b**2 == N:
                reps.append([a,b])
    return reps

def divisors(N):
    """Return the list of divisors of N."""
    # Initialize the list of divisors
    divisor_list = [1]
    # Check division by d for d <= N/2
    for d in range(2,N // 2 + 1):
        if N % d == 0:
            divisor_list.append(d)
    divisor_list.append(N)
    return divisor_list

def n_choose_k(N,K):
    """Compute N choose K."""
    return factorial(N) // (factorial(N - K) * factorial(K))

def factorial(N):
    """Compute N!=N(N-1) ... (2)(1)"""
    # Initialize the outpout variable to 1
    product = 1
    for n in range(2,N + 1):
        # Update the output variable
        product = product * n
    return product

def prime_divisors(N):
    
    def is_prime(a):
        if a<=1:
            return False
        for div in range(2,a):
            if a % div == 0:
                return False
        return True
    
    prime_divisors_list = []
    
    for d in range(1, N // 2 + 1):
        if (N % d == 0) and is_prime(d):
            prime_divisors_list.append(d)
    
    return prime_divisors_list

def is_square(N):
    """Determine whether N is a square number"""
    return N == round(N**(0.5))**2

def rep_as_squares(N):
    """Find all representations of N as a sum of squares a**2 + b**2 = N."""
    reps = []
    stop = int((N/2)**0.5) + 1
    for a in range(1,stop):
        b_squared = N - a**2
        if is_square(b_squared):
            b = round(b_squared**0.5)
            reps.append([a,b])
    return reps
