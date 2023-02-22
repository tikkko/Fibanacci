
def fibonacci(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        print(a)
        a, b = b, a + b
    return





if __name__ == '__main__':
    print(fibonacci(5))