# Encrypt whateve input
# Store the random key and encrypted in 2 files
# Usage: python encrypt.py key cipher_text
#
from sys import argv
from cryptography.fernet import Fernet

script, key_file, cipher_text_file = argv

plain_text = raw_input(">Enter whatever to be encrypted: ")

# Generating random key, then write to key_file
key = Fernet.generate_key()
with open(key_file, 'w') as f:
    f.write(key)

# Encrypting input, then write to cipher_text_file
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(plain_text)
with open(cipher_text_file, 'w') as f:
    f.write(cipher_text)

# Test
print "Generated key: ", key
print "Encrypted: ", cipher_text
print '-' * 4, "Happy coding!", '-' * 4
