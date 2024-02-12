#Hii all This is DAY100(12-02-2024) Today is FInal Day of basics of python so we successfully completed a 100days challenges without any delay
#Today's is simple Program that generate a set of prime numbers and another set of even numbers. Demonstrate the result of union, intersection, difference and symmetirc difference operations.

even=set([x*2 for x in range(1,11)])
primes=set()
for i in range(2,20):
    j=2
    f=0
    while j<=i/2:
        if i%j==0:
            f=1
        j+=1
    if f==0:
        primes.add(i)
print("Even Numbers: ", even)
print("Prime Numbers: ", primes)
print("Union: ", even.union(primes))
print("Intersection: ", even.intersection(primes))
print("Difference: ", even.difference(primes))
print("Symmetric Difference: ", even.symmetric_difference(primes))



#Until this is RS BYE Successfully we completed a 100DAYS BASICS OF PYTHON CHALLENGES
