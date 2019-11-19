# prime.py

def primes():
    x = 100
    primes = []

    for possible_prime in range(1, 10000):
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                break
        else:
            primes.append(possible_prime)
        if len(primes) == x:
            return primes

def main():
    print("OUTPUT", primes())

if __name__ == "__main__":
    main()
