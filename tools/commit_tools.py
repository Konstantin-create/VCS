"""
Tools for commit function file
Functions list:
    - Encode file to BLOB
    - Decode file from BLOB
    - Pretty hash function to print first 4 symbols and last 4 symbols
"""

# Imports
import base64


def encode_file(file_path: str, file_b2_path: str) -> None:
    """Function to encode file"""
    with open(file_path, 'rb') as f:
        file_encoded = base64.b64encode(f.read())
    encoded_b2 = "".join([format(n, '08b') for n in file_encoded])
    with open(file_b2_path, 'w') as file:
        file.write(encoded_b2)


def decode_file(file_b2_path: str, file_path: str) -> None:
    """Function to decode file"""
    with open(file_b2_path, 'r') as file:
        encoded_b2 = file.read()
    decoded_b64 = b"".join([bytes(chr(int(encoded_b2[i:i + 8], 2)), "utf-8") for i in range(0, len(encoded_b2), 8)])
    with open(file_path, 'wb') as file:
        file.write(base64.b64decode(decoded_b64))


def pretty_hash(full_hash):
    """Function for pretty print of sha256 hash in format 1fda...1fu3"""
    return full_hash[:6]
