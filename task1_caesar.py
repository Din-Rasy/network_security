"""Task 1: Caesar cipher encryption and decryption (letters only)."""


def encrypt_caesar(message: str, key: int) -> str:
    result = []
    for char in message:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + key) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + key) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)


def decrypt_caesar(ciphertext: str, key: int) -> str:
    return encrypt_caesar(ciphertext, -key)


if __name__ == '__main__':
    message = 'THURSDAY'
    key = 5
    ciphertext = encrypt_caesar(message, key)
    print('Plaintext :', message)
    print('Key       :', key)
    print('Ciphertext:', ciphertext)
    print('Decrypted :', decrypt_caesar(ciphertext, key))
