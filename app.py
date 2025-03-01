import hashlib
import itertools
import string

# Given SHA-1 hash
target_hash = "32d28d89e1d9e1030478f2e8eb814e907ed56c31"

# Character set (Modify based on expected complexity)
charset = string.ascii_lowercase + string.digits  # a-z, 0-9

# Define max length of password to try
max_length = 6  # Adjust based on complexity

def brute_force_sha1():
    for length in range(1, max_length + 1):  # Start from 1-char passwords
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)  # Convert tuple to string
            hashed_word = hashlib.sha1(word.encode()).hexdigest()  # Hash it
            
            if hashed_word == target_hash:
                print(f"\n[+] Hash cracked! The password is: {word}")
                return
            
            print(f"[-] Trying: {word}", end="\r")  # Live status update
    
    print("\n[-] Password not found. Try increasing max_length or changing charset.")

# Start brute force attack
brute_force_sha1()
