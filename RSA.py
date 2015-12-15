from random import SystemRandom

class RSA:
    def __init__(self, bits):
        self.random = SystemRandom()
        return
    
    def extended_euclidean(self, totn, prime):
        return
    
    def miller_rabin_primality_test(self, n, iterations):

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
    
    def gen_primes(self, bits):
        return

    def encrypt(self, message):
        return

    def decrypt(self, cypher):
        return

    def get_public_key(self):
        return

    def get_private_key(self):
        return
