import hashlib

def md5_hash(data):
    # Ma'lumotni MD5 hashiga o'zgartirish
    md5_hasher = hashlib.md5()
    md5_hasher.update(str(data).encode('utf-8'))
    md5_hashed_data = md5_hasher.hexdigest()
    return md5_hashed_data

# Funksiyani sinash
input_data = 12345  # Kiruvchi ma'lumot (integer)
hashed_data = md5_hash(input_data)
print("MD5 hashlash natijasi:", type(hashed_data))
