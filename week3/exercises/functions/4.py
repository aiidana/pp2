from math import*
n=int(input())
def is_prime(n): 
    if n==2:
        return True
    if n%2==0:
        return False
    return all(n%x for x in range(3, int(sqrt(n)), 2))

print("Prime") if is_prime(n) else print("No prime")
