import os
import hashlib

"""
    A function that processes input data.
    This is just a placeholder function for testing.
    In a real-world scenario, this might perform some complex operations
    like parsing, data validation, or transformation.
    """
def insecure_password_handling():
    password = "1234"
    print(password)



"""
    A function that processes input data.
    This is just a placeholder function for testing.
    In a real-world scenario, this might perform some complex operations
    like parsing, data validation, or transformation.
    """
def insecure_md2_hash():
    # MD2 is a weak and insecure hash function.
    data = "example data".encode('utf-8')
    md2_hash = hashlib.new('md2', data)  # B303: MD2 is blacklisted
    print(md2_hash.hexdigest())

if __name__ == "__main__":
    insecure_password_handling()
    insecure_md2_hash()


