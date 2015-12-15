from random import SystemRandom

class RSA:
    def __init__(self, bits, RMiterations=64):
        self.random = SystemRandom()
        self.RMi = RMiterations
        self.bits = bits
    
    def extended_euclidean(self, totn, prime):
        return
    
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

    def encrypt(self, message):
        return

    def decrypt(self, cypher):
        return

    def get_public_key(self):
        return

    def get_private_key(self):
        return
