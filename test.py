import hashlib

# Module docstring added
"""
This module demonstrates the use of insecure functions and hashing algorithms 
for educational purposes. It includes functions to handle passwords and 
generate weak hashes like MD2.
"""

def insecure_password_handling():
    """
    A function that demonstrates insecure passwords handling.
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
