def factorial(num):
    ans = 1
    
    for i in range(1, num+1):
        ans *= i
    
    print(f"{num}! = {ans}")
    
def sum(num):
    total = 0
    
    for i in range(1, num+1):
        total += i
    
    print(f"sum 1 to {num} = {total}")
    
def power(base, exp):
    ans = 1
    
    for i in range(exp):
        ans *= base
        
    print(f"{base}^{exp} = {ans}")
    
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            return #exits function
        
    print(f"{num} is prime")

# Math Program
print("Weclome to my math game!!!")

while True:
    command = input("(S)um, (P)ower, (F)actorial, P(R)ime, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "s":
        num = int(input("Enter Number: "))
        sum(num)
    elif command == "p":
        base = int(input("Enter Base: "))
        exp = int(input("Enter Exponent: "))
        power(base, exp)
    elif command == "f":
        ans = int()
    elif command == "r":
        

    
        print("Goodbye")