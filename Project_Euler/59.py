'''
XOR decryption
Problem 59
'''


from collections import Counter

to_decode = list(map(int, open('p059_cipher.txt').read().split(',')))
key = [Counter(to_decode[i::3]).most_common(1)[0][0] ^ 32 for i in range(3)]
print("Key:", ''.join(list(map(chr, key))))
print("Result:", sum(x ^ y for x, y in zip(to_decode, key*(len(to_decode)//3+1))))
