# Solution using for loop
def get_factorial_using_for_loop(num):
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    return ans

# Solution using for while
def get_factorial_using_while_loop(num):
    ans = 1
    i = 1
    while i <= num:
        ans *= i
        i += 1
    return ans 
# Calling Functions
num = 4
print(f"Factorial of {num} using for loop =  {get_factorial_using_for_loop(num)}")
print(f"Factorial of {num} using while loop= {get_factorial_using_while_loop(num)}")