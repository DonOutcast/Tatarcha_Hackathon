from cryptography.fernet import Fernet

# Шифруем
cipher_key = Fernet.generate_key()
cipher = Fernet(cipher_key)
text = b'Message'
encrypted_text = cipher.encrypt(text)
print(encrypted_text)
print("\n")

# Дешифруем
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text)

input()