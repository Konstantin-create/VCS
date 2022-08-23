"""
Functions to work with hashlib
Functions:
    - Generate hash from binary string
"""

# Imports
import hashlib


def generate_hash(b_string: bytes) -> str:
    """Generate hash from binary string"""

    return hashlib.sha256(b_string).hexdigest()
