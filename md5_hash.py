import hashlib

def sha256_hash(data):
    # Ma'lumotni SHA-256 hashiga aylantirish
    data = str(data)
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))  # Ma'lumotni enkod qilish
    return sha256_hash.hexdigest()
