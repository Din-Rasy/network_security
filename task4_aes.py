"""Task 4: AES-128-GCM encryption, decryption, and tamper detection."""
import os
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def demonstrate(message: bytes) -> None:
    key = AESGCM.generate_key(bit_length=128)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(nonce, message, None)
    decrypted = aes.decrypt(nonce, ciphertext, None)

    print('Key       :', key.hex())
    print('Nonce     :', nonce.hex())
    print('Plaintext :', message.decode('utf-8'))
    print('Ciphertext:', ciphertext.hex())
    print('Decrypted :', decrypted.decode('utf-8'))

    modified = bytearray(ciphertext)
    modified[0] ^= 1
    try:
        aes.decrypt(nonce, bytes(modified), None)
        print('ERROR: Unexpectedly accepted modified ciphertext!')
    except InvalidTag:
        print('WARNING: Message was modified!')


if __name__ == '__main__':
    print('Exercise 4.1 (run twice to compare randomly generated values):')
    demonstrate(b'Welcome to Network Security')
    print('\nExercise 4.2 (modified plaintext):')
    demonstrate(b'My password is 123456')  # Illustrative lab message only; not a real password.
