def factorial(n):
    factorial_total = 1

    while n >= 1:

        factorial_total = factorial_total *n
        n = n -1

    return factorial_total

        
        

   


n = int(input("enter in a number"))
ans = factorial(n)
ans = "factorial of entered number is " + repr(ans)
print(ans)
