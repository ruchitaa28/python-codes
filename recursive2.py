def binary(n):
    if n == 0:
        return ''
    return binary(n // 2) + str(n % 2)
n = int(input("Enter a positive integer: "))
print(binary(n))
