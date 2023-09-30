
def find_m_and_k(number):
    m = number
    k = 0

    while m % 2 == 0:
        m //= 2
        k += 1

    return m, k






def millerRabin(n, a):
    if n==1 or n==2: return "a prime"
    # Find m and k
    m, k = find_m_and_k(n-1)
    print("m:{}".format(m))
    print("k: {}".format(k))

    T=pow(a, m, n)
    # print(T)
    
    if T==1 or T==n-1: 
        return "a prime"
    else:
        for x in range(1,k):
            T=pow(T,2,n)
            # print(T)
            if T==n-1: return "a prime"
            if T==1: return "a composite"
    return "a composite"

n=67
print("{0} is {1}".format(n, millerRabin(67,2)))


