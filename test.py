import os
import hashlib

# Added module docstring to avoid 'missing-module-docstring' error
"""
Module to demonstrate various functions with examples of good and bad practices
"""

def insecure_password_handling():
    """
    A function that demonstrates insecure password handling.
    In a real-world scenario, this should not be hardcoding passwords.
    """
    password = "1234"
    print(password)

def insecure_md2_hash():
    """
    A function that demonstrates insecure MD2 hashing.
    MD2 is considered weak and should not be used in practice.
    """
    # MD2 is a weak and insecure hash function.
    data = "example data".encode('utf-8')
    md2_hash = hashlib.new('md2', data)  # B303: MD2 is blacklisted
    print(md2_hash.hexdigest())

if __name__ == "__main__":
    insecure_password_handling()
    insecure_md2_hash()
