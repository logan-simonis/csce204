
def factorial(num):
    ans = 1
    
    for i in range(1, num+1):
        ans *= i
    
    print(f"{num}! = {ans}")
    
# displays the sum of 1 to num
# e.g. sum 5 = 5+4+3+2+1=15
def sum(num):
    total = 0
    
    for i in range(1, num+1):
        total += i
    
    print(f"sum 1 to {num} = {total}")
     
# test sum
# sum(5)

# calculates the power
# e.g. 2^3 = 2 * 2 * 2
def power(base, exp):
    ans = 1
    
    for i in range(exp):
        ans *= base
        
    print(f"{base}^{exp} = {ans}")
       
#test
#power(2,3)

#displays either num is prime or num is not prime
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            return #exits function
        
    print(f"{num} is prime")   # no number event divided
    
# test
is_prime(12)
#is_prime(11)