
# Bandit is a tool designed to find common security issues in Python code.
# To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes.
# Once Bandit has finished scanning all the files, it generates a report.
import os
import non_existent_module  # E0401: Unable to import 'non_existent_module'


result =[] #usused variable

def insecure_function():
    myVariable = 10878 #snake_case naming error

    user_input = input("Enter something: ")
    os.system(f"echo {user_input}")  # Vulnerable to command injection


# def func():   # E0001: SyntaxError
#     print('hello'


def insecure_password_handling():
    password = "1234"
    print(password)


# test_line_too_long.py

def process_data(input_data):
    """
    A function that processes input data.
    This is just a placeholder function for testing.
    In a real-world scenario, this might perform some complex operations
    like parsing, data validation, or transformation.
    """
    print(f"Processing data: {input_data[:50]}...")  # Print the first 50 characters


def test_line_too_long():
    res= []
# length for a line of code. A line length over 79 characters is typically flagged
    #by style checkers like PEP 8, flake8, or pylint.This function demonstrates the problem of a
    long_line = (
            "a" * 1500
    )

    # Here, the function would normally process the input in some way
    # that makes sense in the context of your application.
    process_data(long_line)  # Pass the long line to the processing function

    # Simulate some other processing logic.
    print("Processing complete.")

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

def insecure_md5_hash():
    # MD5 is insecure and should not be used for security-related purposes.
    data = "example data".encode('utf-8')
    md5_hash = hashlib.md5(data)  # B303: MD5 is blacklisted
    print(md5_hash.hexdigest())



if __name__ == "__main__":
    insecure_function()
    insecure_password_handling()
    test_line_too_long()
    missingfunction()
    insecure_md5_hash()

