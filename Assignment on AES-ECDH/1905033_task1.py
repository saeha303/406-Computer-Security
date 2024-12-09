import _1905033_utils
import time

# Thats my Kung Fu
# Two One Nine Two
# BUET CSE19 Batch
# Never Gonna Give you up
N = 3

def rounds(i, j, temp_matrix, encrypt):
    if j == 0:
        temp_matrix = round0(i, j, encrypt)
        return temp_matrix
    else:
        if encrypt:
            temp_matrix = _1905033_utils.sub_bytes(temp_matrix, count, encrypt)
            temp_matrix = _1905033_utils.shift_row(temp_matrix, encrypt)
            if (j == 14 or j == 12 or j == 10):
                temp_matrix = _1905033_utils.add_round_key(temp_matrix, R, j, encrypt)
            else:
                temp_matrix = _1905033_utils.mix_columns(temp_matrix, encrypt)
                temp_matrix = _1905033_utils.add_round_key(temp_matrix, R, j, encrypt)
        else:
            temp_matrix = _1905033_utils.shift_row(temp_matrix, encrypt)
            temp_matrix = _1905033_utils.sub_bytes(temp_matrix, count, encrypt)
            if (j == 14 or j == 12 or j == 10):
                temp_matrix = _1905033_utils.add_round_key(temp_matrix, R, j, encrypt)
            else:
                temp_matrix = _1905033_utils.add_round_key(temp_matrix, R, j, encrypt)
                temp_matrix = _1905033_utils.mix_columns(temp_matrix, encrypt)

        return temp_matrix


def round0(i, j, encrypt):
    # iv = _1905033_utils.generate_iv(intended_len).hex()
    if i==0 and encrypt:
        temp_matrix = _1905033_utils.xor(plain_matrix[i], iv)
    else:
        temp_matrix = plain_matrix[i]
    temp_matrix = _1905033_utils.add_round_key(temp_matrix, R, j, encrypt)
    return temp_matrix

# intended_len = input('Intended message length: ')
intended_len='128'
print('Key:')
key = input("In ASCII: ")
print('In HEX: ')
key_matrix = _1905033_utils.string_to_array(key, intended_len)
print(' '.join(map(str, key_matrix)))
print('Plain text:')
plain = input("In ASCII: ")
plain_matrix = _1905033_utils.string_to_matrix(plain, intended_len)
for row in plain_matrix:
    print(' '.join(map(str, row)))

R = 0
count = 0
if intended_len == '128':
    R = 11
    count = 16
elif intended_len == '192':
    R = 13
    count = 24
elif intended_len == '256':
    R = 15
    count = 32
start_time = time.time()
_1905033_utils.key_scheduling(key_matrix)
key_scheduling_time = time.time() - start_time
# iv = ['51', 'b8', 'bc', '3d', '90', '42', '51', '37', '54', '53', '69', '56', '43', '50', 'cc', 'a0']
iv=_1905033_utils.generate_iv(intended_len)
temp_matrix = [0] * count
encrypt = True
start_time = time.time()
for i in range(len(plain_matrix)):
    for j in range(R):
        temp_matrix = rounds(i, j, plain_matrix[i], encrypt)
        plain_matrix[i] = temp_matrix
    if i < len(plain_matrix) - 1:
        plain_matrix[i + 1] = _1905033_utils.xor(plain_matrix[i + 1], plain_matrix[i])
encryption_time = time.time() - start_time
print('Ciphered text:')
formatted_matrix = ' '.join([' '.join(row) for row in plain_matrix])
print('In HEX: ', formatted_matrix)
hex_values = formatted_matrix.split()
ascii_characters = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])
print("In ASCII: ", ascii_characters)
encrypt = False
prev = plain_matrix[0]
start_time = time.time()
for i in range(len(plain_matrix)):
    row = plain_matrix[i]
    for j in range(R):
        plain_matrix[i] = rounds(i, j, plain_matrix[i], encrypt)
    if i == 0:
        plain_matrix[i] = _1905033_utils.xor(plain_matrix[i], iv)
    else:
        plain_matrix[i]=_1905033_utils.xor(plain_matrix[i],prev)
        prev=row
decryption_time = time.time() - start_time
print('Deciphered text:')
formatted_matrix = ' '.join([' '.join(row) for row in plain_matrix])
print('In HEX: ', formatted_matrix)
hex_values = formatted_matrix.split()
ascii_characters = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])
print("In ASCII: ", ascii_characters)

print('Execution time details')
print('Key schedule time: ',key_scheduling_time*1000,' ms')
print('Encryption time: ',encryption_time*1000,' ms')
print('Decryption time: ',decryption_time*1000,' ms')