"""Task 3: Compare deterministic pseudo-random numbers with secrets."""
import random
import secrets


if __name__ == '__main__':
    random.seed(1234)
    print('Predictable values (same on each run):')
    for _ in range(3):
        print(random.randint(0, 1000000))

    print('\nSecure random values:')
    for _ in range(3):
        print(secrets.token_hex(16))
