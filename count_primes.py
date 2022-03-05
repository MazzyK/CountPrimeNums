def get_range():
    return int(input("up to which number do you want to count primes?"))


def count_primes(n):
    is_prime=True
    primes=[2]

    for i in range (3,n,2):
        for j in range(i-1,1,-1):
            if i%j==0:
                is_prime=False
                break
            else:
                is_prime=True
        if is_prime:
            primes.append(i)
    print("there are {} prime numbers between 1 and {}. These are:".format(len(primes),n))

    return primes


print(count_primes(get_range()))
