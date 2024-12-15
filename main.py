import math
import random

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        return True
def genarate_prime(min_value, max_value):
    prime = random.randint(min_value,max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return  prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Mod inverse does not exist")


p, q = genarate_prime(1000,5000), genarate_prime(1000,5000)

while p == q:
    genarate_prime(1000,5000)

n = p * q
phi_n = (p-1) * (q-1)
e = random.randint(3, phi_n-1)
while math.gcd(e,phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e,phi_n)


message = "Hello World"
message_encoded = [ord(ch) for ch in message]
cipertext = [pow(ch, e, n) for ch in message_encoded]
message = "".join(chr(ch) for in message_encoded)
# Decode message
message_encoded = [pow(ch, d, n) for ch in cipertext]
print(cipertext)
