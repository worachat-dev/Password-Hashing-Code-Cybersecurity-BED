# -*- coding: utf-8 -*-
"""My Password Hashing Code in Cybersecurity

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xi-TOWcs7UgqFOyJSGkVB8dGGznFqVo4

## HASHING IN CYBERSECURITY by Worachat Wannawong, Ph.D.

**Understanding the Code**

The provided code implements basic password hashing using PBKDF2-HMAC with SHA-256. It stores hashed passwords in a simple in-memory dictionary.

**Potential Issues and Improvements**

1. **Password Storage:**
   - Storing passwords in plain text, even hashed, is highly insecure. Consider using a secure password storage mechanism like a database with proper encryption.
   - For a simple demonstration, you could use environment variables or configuration files to store hashed passwords securely.

2. **Salt Storage:**
   - The salt is currently concatenated with the hashed password. This is not ideal as it exposes the salt, which can potentially be used for dictionary attacks.
   - Store the salt separately from the hashed password.

3. **Password Complexity:**
   - Implement password complexity checks to enforce strong password policies.
   - Use regular expressions or password strength libraries to validate password format.

4. **Error Handling:**
   - Add error handling for exceptions like invalid input, file operations, or database interactions.

5. **Code Organization:**
   - Consider using classes or modules to better organize the code, especially for larger projects.

6. **Security Best Practices:**
   - Increase the iteration count for PBKDF2 to improve security.
   - Use a more secure hashing algorithm if available.
   - Consider using key derivation functions like Argon2 for even stronger protection.

**Provided Code**
In the provided code, the `database` dictionary contains two usernames: `"clcoding"` and `"pythonclcoding"`. These are the usernames you can use to test the program.

For example:
- **Username:** `clcoding`
- **Password:** `976729`

- **Username:** `pythonclcoding`
- **Password:** `2502`

Make sure you enter the usernames exactly as they appear in the `database` dictionary, including the correct case, as string comparisons in Python are case-sensitive. If the username you enter doesn't match any key in the dictionary, the program will output "Username not found."
"""

import hashlib
import os
import getpass

def hash_password(password: str) -> str:
    """
    Hashes a password using PBKDF2 HMAC with SHA-256 and a randomly generated salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        tuple: The salt and hashed password as byte strings.
    """
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000  # Increase iteration count for better security
    )
    return salt, hashed_password

def verify_password(stored_salt: bytes, stored_hash: bytes, provided_password: str) -> bool:
    """
    Verifies a provided password against the stored hashed password.

    Args:
        stored_salt (bytes): The stored salt.
        stored_hash (bytes): The stored hashed password.
        provided_password (str): The password to verify.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode(),
        stored_salt,
        100000
    )
    return hashed_password == stored_hash

# Replace with secure password storage
database = {
    "clcoding": hash_password("976729"),
    "pythonclcoding": hash_password("2502")
}


if __name__ == "__main__":
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")

    if username in database:
        salt, stored_hash = database[username]
        if verify_password(salt, stored_hash, password):
            print("Verified")
        else:
            print("Invalid password. Please try again.")
    else:
        print("Username not found.")

import hashlib
import os
import getpass

def hash_password(password: str) -> tuple:
    """
    Hashes a password using PBKDF2 HMAC with SHA-256 and a randomly generated salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        tuple: The salt and hashed password as byte strings.
    """
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000  # Increase iteration count for better security
    )
    return salt, hashed_password

def verify_password(stored_salt: bytes, stored_hash: bytes, provided_password: str) -> bool:
    """
    Verifies a provided password against the stored hashed password.

    Args:
        stored_salt (bytes): The stored salt.
        stored_hash (bytes): The stored hashed password.
        provided_password (str): The password to verify.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode(),
        stored_salt,
        100000
    )
    return hashed_password == stored_hash

# Example user data with hashed passwords
database = {
    "clcoding": hash_password("976729"),
    "pythonclcoding": hash_password("2502")
}

if __name__ == "__main__":
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")

    if username in database:
        stored_salt, stored_hash = database[username]
        if verify_password(stored_salt, stored_hash, password):
            print("Verified")
        else:
            print("Invalid password. Please try again.")
    else:
        print("Username not found.")

"""**Additional Considerations:**

- For production environments, consider using a dedicated password hashing library like `bcrypt` or `argon2_cffi` for more advanced features and security.
- Implement proper error handling and input validation.
- Explore using a key management system to handle salts and hashed passwords securely.

By following these improvements, you can significantly enhance the security of your password hashing implementation.

**Would you like to explore any of these points in more detail?**
"""