from cryptography.fernet import Fernet

def plain_text(file_key, file_cipher_text):
    """Return plain_text with provided paths of key and cipher_text files"""
    with open(file_key, 'r') as f:
        key = f.readline()
    with open(file_cipher_text, 'r') as f:
        cipher_text = f.readline()

    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(cipher_text)

# Test
file_key = '/home/user/.keys/key'
file_cipher_text = '/home/user/.keys/cipher_text'
print plain_text(file_key, file_cipher_text)
print '-' * 10
