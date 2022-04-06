"""
Section 4  Test Code

In testing the hypotheses of the main theorem we utilized the following code. In the initial attempt we investigated the ZIP group. (That is, Z mod p adjoin i where -1 is a quadratic non residue or ZIP = Fp^2 with p congruent to 3 mod 4). Later the result is generalized for prime p and integer n, a quadratic non residue.
The code can be easily expanded to general p and n.
"""
if __name__ == "__main__":
    print("In main")

    print("Enter a prime")
    prime = int(input())

class Primes:
    def __init__(self, num):
        self.num = num        

    def find_primes(self):
        primes = []        
        for i in range (2, self.num+1):
           primes.append(i)       
        notprimes = []
        for i in range (2,self.num+1):    
            for j in range (i+1,self. num+1):        
                if j%i == 0:
                    if notprimes.count(j) == 0:
                        notprimes.append(j)        
        for i in notprimes:
            primes.remove(i)                
        return primes
    
# for example is prime congruent to 3 mod 4
    def is_prime_con(self, prime, con, mod):
        if prime%mod == con:
            return True
        return False
    
# for example find primes congruent to 3 mod 4
    def find_primes_con(self, con, mod):        
        primes = self.find_primes()
        con_primes = []
        for p in primes:
            if self.is_prime_con( p, con, mod):
                con_primes.append(p)
        return con_primes
    
# Z modulo p* 
class ZModP:
    def __init__(self, prime):
        self.prime = prime

    def is_element_primitive_root(self, element):
        prime = self.prime
        for i in range(1, prime):
            if element**i % prime == 1 and i < prime - 1:
                return False
        return True
        
    def find_primitive_roots(self):
        p = self.prime
        primitive_roots = []
        for i in range(1,p):
            if self.is_element_primitive_root(i):              
                primitive_roots.append(i)
        return primitive_roots

    def find_inverse(self, element):
        inverse = 1
        p = self.prime
        for b in range (p):
            if b*element % p == 1:
                inverse = b
                break
        return inverse

#quadratic residues
class QuadraticResidues:
    def __init__(self, prime):
        self.prime = prime
        
    def is_quadratic_residue(self, num):
        p = self.prime
        for i in range (1, p):
            if (num % p) == (i**2 %p):
                return True
        return False

    def find_quadratic_residues(self):
        residues = []
        p = self.prime
        for i in range (1, p):
            if self.is_quadratic_residue(i):
                residues.append(i)
        return residues
        

# Z modulo p adjoin i (primes congruent to 3 mod 4)
class ZIP:
    def __init__(self, prime):
        self.prime = prime
        
    def raise_zip_to_power(self, exp, a, b):
        p = self.prime
        real = a
        imag = b
        if exp == 1:
            return [a%p,b%p]
        for i in range(2,exp+1):
            tempreal = (real*a - imag*b)%p
            imag = (real*b + imag*a)%p
            real = tempreal        
        return [real,imag]

    def find_order(self, a, b):
        p = self.prime
        order = 0
        for i in range (1, p**2):
            power = self.raise_zip_to_power(i, a, b)
            if power[0] == 1  and power[1] == 0:
                order = i
                break
        return order
    
    def multiply_zips(self, a, b, c, d):
        p = self.prime
        return [(a*c - b*d)%p, (a*d + b*c)%p]
    
    def find_inverse(self, a, b):
        p = self.prime
        inverse = [1,0]
        product = [0,0]    
        for c in range (p):
            for d in range (p):
                product = self.multiply_zips(a, b, c, d)
                if product[0] == 1 and product[1]==0:
                    inverse = [c,d]
                    break        
        return inverse

    def find_generators_for_zip(self):
        p = self.prime
        counter = 0
        result = 0
        order = 0
        generators = []            
        for a in range(p):
            for b in range(p):
                order = self.find_order(a, b)
                if order == p**2-1:
                    generators.append([a,b])
        print(len(generators))
        return generators

    def is_element_generator(self, a, b):
        p = self.prime        
        if self.find_order(a, b)== p**2-1:
            return True
        return False

# class specific to the homomorphism ZIP -> Zp f(a+ib) = a^2 + b^2
class SquareKernel:
    def __init__(self, prime):
        self.prime = prime

    def is_element_in_kernel(self, a, b):
        p = self.prime
        if (a**2 + b**2)%p == 1:
            return True
        return False
    
    def is_element_generator_of_kernel(self,a, b):
        p = self.prime
        zpi = ZIP(p)
        if self.is_element_in_kernel(a,b) and zpi.find_order(a,b) == p+1:
            return True
        return False

    def find_elements_of_the_kernel(self):
        p = self.prime
        kernel = []
        for a in range(p):
            for b in range(p):
                if self.is_element_in_kernel(a, b):
                    kernel.append([a,b])
        return kernel
                
        
    def find_generators_of_the_kernel(self):
        p = self.prime
        generators = []
        for a in range(p):
            for b in range(p):
                if self.is_element_generator_of_kernel(a, b):
                    generators.append([a,b])
        return generators
    
# class specific to testing the hypotheisis of the theorem for the ZIP group i.e. if a^2 + b^2 has order p-1 (primitive root for Zp*) and
# (a^2 - b^2)/(a^2 +b^2) + 2abi/(a^2 + b^2) has order p+1 (generates kernel) iff a+bi generates ZIP
class Conjecture:
    def __init__(self, prime):
        self.prime = prime
    
    def find_order_of_image_kernel_element(self, a, b):
        p = self.prime
        zp = ZModP(p)
        zpi = ZIP(p)
        inverse = zp.find_inverse((a**2 + b**2)%p)
        return zpi.find_order(((a**2 - b**2)%p)*inverse, ((2*a*b)%p)*inverse)
# ->
    def two_generators_imply_generator(self):
        p = self.prime
        zp = ZModP(p)
        zpi = ZIP(p)
        count = 0
        for a in range(p):
            for b in range(p):
                if a != 0 or b!= 0:                    
                    if zp.is_element_primitive_root(a**2 + b**2):
                        if self.find_order_of_image_kernel_element(a, b) == p+1:
                            order = zpi.find_order(a,b)
                            count = count + 1
                            if order != p**2 - 1:
                                return False                            
        return True
# <-
    def generator_implies_two_generators(self):
        p = self.prime
        zpi = ZIP(p)
        zp = ZModP(p)
        for a in range(p):
            for b in range(p):
                if zpi.is_element_generator(a, b):
                    if zp.is_element_primitive_root(a**2 + b**2) == False or self.find_order_of_image_kernel_element(a, b) !=  p+1:
                        return False                    
        return True    

if __name__ == "__main__":
    #execute test code
    
    
