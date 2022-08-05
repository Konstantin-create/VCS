import hashlib


def generate_hash(b_string):
    return hashlib.sha256(b_string).hexdigest()
