from Crypto.Util import number
from sympy.ntheory import totient
from sympy import mod_inverse
from sympy import gcd
import random

class Paillier:
    
    # key generation function
    def key_generation(self, bit_length):
        self.p_bit_length = bit_length
        self.q_bit_length = bit_length

        p = number.getPrime(bit_length)
        q = number.getPrime(bit_length)

        n = p * q
        g = n + 1

        #lambda_ = math.lcm(p - 1, q - 1)
        lambda_ = int(totient(n))

        mu = mod_inverse(lambda_, n)
        
        self.public_key = (n, g)
        self.private_key = (lambda_, mu)
        return self.public_key, self.private_key

    # Encryption function
    def encrypt(self, public_key, m):
        n, g = public_key
        nsq = n * n
        while True:
            r = random.randint(1, n - 1)
            if gcd(r, n) == 1:
                break
        c = (pow(g, m, nsq) * pow(r, n, nsq)) % nsq
        return c

    # Decryption function
    def decrypt(self, public_key, private_key, c):
        n, g = public_key
        nsq = n * n
        lambda_val, mu = private_key
        x = pow(c, lambda_val, nsq)
        l = (x - 1) // n
        m = (l * mu) % n
        return m

