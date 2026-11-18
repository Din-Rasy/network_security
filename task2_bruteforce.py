"""Task 2: Test all 25 non-identity Caesar keys."""
from task1_caesar import encrypt_caesar, decrypt_caesar


if __name__ == '__main__':
    original_message = 'THURSDAY'
    correct_key = 5
    ciphertext = encrypt_caesar(original_message, correct_key)
    print('Ciphertext:', ciphertext)
    print('Trying all 25 possible non-zero shifts:\n')
    for key in range(1, 26):
        plaintext = decrypt_caesar(ciphertext, key)
        print('Key', key, ':', plaintext)
