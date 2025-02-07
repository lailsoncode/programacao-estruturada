# def fatorial(n):
#     resultado = 1
#     for numero in range(1, n):
#         resultado *= numero
    
#     return resultado

# # fatorial(6)
# print(fatorial(6))


# def fatorial_r(n):
#     if n == 0 or n == 1:
#         return n
#     return n * fatorial_r(n - 1)

# print(fatorial_r(999))

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(33))