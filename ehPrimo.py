def ehPrimo(n):
    k = n - 1
    while k > 1:
        if n % k != 0:
            k -= 1
        else:
            return False
    return True

n = int(input())
while n > 0:
    if ehPrimo(n) == True:
        print(n, 'é primo')
    else:
        print(n, 'não é primo')
    n = int(input())