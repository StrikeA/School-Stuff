import numpy as np
import math

# Define the Hill cipher encryption and decryption functions
def encrypt(message, key):
    # Convert the message to uppercase
    message = message.upper()
    # Calculate the size of the square matrix
    n = int(math.sqrt(len(key)))
    # Reshape the key into a square matrix
    key_matrix = np.reshape(np.array(list(key)), (n, n))
    # Create a list to hold the numerical values of the message
    message_nums = []
    # Convert the message to numerical values
    for letter in message:
        message_nums.append(ord(letter) - 65)
    # Reshape the message into a matrix
    message_matrix = np.reshape(np.array(message_nums), (-1, n))
    # Add padding to the message if necessary
    if len(message) % n != 0:
        message_matrix = np.pad(message_matrix, ((0, n - len(message) % n), (0, 0)), mode='constant', constant_values=0)
    # Multiply the key matrix by the message matrix
    result_matrix = np.matmul(key_matrix, message_matrix) % 26
    # Convert the result matrix to a string
    result = ''
    for row in result_matrix:
        for num in row:
            result += chr(num + 65)
    return result

def decrypt(ciphertext, key):
    # Convert the ciphertext to uppercase
    ciphertext = ciphertext.upper()
    # Calculate the size of the square matrix
    n = int(math.sqrt(len(key)))
    # Reshape the key into a square matrix
    key_matrix = np.reshape(np.array(list(key)), (n, n))
    # Inverse the key matrix
    key_matrix_inv = np.linalg.inv(key_matrix)
    # Calculate the determinant of the key matrix
    det = int(round(np.linalg.det(key_matrix)))
    # Calculate the modular inverse of the determinant
    det_inv = -1
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    # Calculate the adjugate of the key matrix
    adj = det * key_matrix_inv
    adj = adj.round().astype(int) % 26
    adj = np.transpose(adj)
    # Create a list to hold the numerical values of the ciphertext
    ciphertext_nums = []
    # Convert the ciphertext to numerical values
    for letter in ciphertext:
        ciphertext_nums.append(ord(letter) - 65)
    # Reshape the ciphertext into a matrix
    ciphertext_matrix = np.reshape(np.array(ciphertext_nums), (-1, n))
    # Multiply the adjugate matrix by the ciphertext matrix
    result_matrix = np.matmul(adj, ciphertext_matrix) % 26
    # Convert the result matrix to a string
    result = ''
    for row in result_matrix:
        for num in row:
            result += chr(num + 65)
    return result

# Ask the user if they want to encrypt or decrypt a message
while True:
    mode = input("Do you want to encrypt or decrypt a message? ")
    if mode.lower() == 'encrypt' or mode.lower() == 'decrypt':
        break

# Ask the user for the message and key
message = input("Enter the message: ")
key = input("Enter the key: ")

# Encrypt or decrypt the message based on the user's choice
if mode.lower() == 'encrypt':
    ciphertext = encrypt(message, key)
    print("The encrypted message is:", ciphertext)
else:
    pass
