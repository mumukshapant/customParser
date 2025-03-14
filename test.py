import os

def insecure_function():
    my_ariable = 10 #snake_case naming error


def insecure_password_handling():
    password = "1234"
    print(password)

import hashlib

def insecure_md2_hash():
    # MD2 is a weak and insecure hash function.
    data = "example data".encode('utf-8')
    md2_hash = hashlib.new('md2', data)  # B303: MD2 is blacklisted
    print(md2_hash.hexdigest())

def insecure_md4_hash():
    # MD4 is also a weak hash function.
    data = "example data".encode('utf-8')
    md4_hash = hashlib.new('md4', data)  # B303: MD4 is blacklisted
    print(md4_hash.hexdigest())


if __name__ == "__main__":
    insecure_function()
    insecure_password_handling()


