from random import SystemRandom

class RSA:
    def __init__(self, bits, RMiterations=64):
        self.random = SystemRandom()
        self.RMi = RMiterations
        self.bits = bits

        p, q = self.gen_primes()
        self.n = p*q
        
        totient = (p-1) * (q-1) 
        self.public_key = 65537
        self.private_key = self.extended_euclidean(totient, self.public_key)
        
    def extended_euclidean(self, totient, p):
        '''
        Returns the multiplicative inverse of p wrt totient.
        Adapted from: https://goo.gl/Zyh7T1
        '''
        original_totient = totient
        x,y, u,v = 0,1, 1,0
        while totient != 0:
            q, r = p//totient, p%totient
            m, n = x-u*q, y-v*q
            p,totient, x,y, u,v = totient,r, u,v, m,n
        
        return y if y > 0 else y + original_totient
            
    
    def rabin_miller_primality_test(self, n, iterations):

        #Break n-1 into 2^r * d where d is odd
        r = 0
        d = n - 1 
        while d%2 == 0:
            r += 1
            d = d / 2
        #return (r,d)

        
        for _ in xrange(iterations):
            a = self.random.randint(2,n-2)
            x = pow(a, d, n) #(a**d)%n
            
            if x == 1 or x == n - 1:
                continue

            for __ in xrange(r-1):
                x = pow(x, 2, n)
                
                if x == 1:
                    return False
                if x == n - 1:
                    break
            
            else:
                #If no x == n - 1
                return False

        return True
        
    def OAEP(self, message):
        return
    
    def gen_primes(self):
        max_number = 2**self.bits
        
        p = self.random.randint(2,max_number)
        if not p%2:
            p -= 1 #Ensure p is odd
        while not self.rabin_miller_primality_test(p, self.RMi):
            p += 2

        q = self.random.randint(2,max_number)
        if not q%2:
            q -= 1 #Ensure q is odd
        while not self.rabin_miller_primality_test(q, self.RMi):
            q += 2 
        
        return (p,q)

    def encrypt(self, message, pub_key, n):
        if type(message) != int:
            raise TypeError('Message must be an integer')
        elif message > n:
            raise ValueError('Message is too large to encrypt')
        
        return pow(message, pub_key, n)

    def decrypt(self, cypher):
        return pow(cypher, self.private_key, self.n)

    def signed_hash(self, cypher, pub_key, n):
        '''
        Returns a decrypted hash used to verify a signed message.
        '''
        return pow(cypher, pub_key, n)

    def get_public_key(self):
        return

    def get_private_key(self):
        return
