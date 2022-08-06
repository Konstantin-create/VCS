import hashlib


def generate_hash(b_string: bytes) -> str:
    return hashlib.sha256(b_string).hexdigest()
