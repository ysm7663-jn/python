import hashlib

data = input()
encoded_data = data.encode()
result = hashlib.sha256(data).hexdigest()
print(result)
