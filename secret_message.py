"""Task 5: Encrypt a user-provided message with AES-128-GCM."""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def main() -> None:
    message = input('Enter your secret message: ')
    key = AESGCM.generate_key(bit_length=128)
    nonce = os.urandom(12)
    aes = AESGCM(key)

    ciphertext = aes.encrypt(nonce, message.encode('utf-8'), None)
    print('Ciphertext:', ciphertext.hex())
    recovered = aes.decrypt(nonce, ciphertext, None)
    print('Decrypted :', recovered.decode('utf-8'))


if __name__ == '__main__':
    main()
