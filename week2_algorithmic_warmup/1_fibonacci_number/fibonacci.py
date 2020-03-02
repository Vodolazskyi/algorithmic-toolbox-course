# Uses python3
def calc_fib(n: int) -> int:
    if (n <= 1):
        return n

    prev2 = 0
    prev1 = 1
    for i in range(2, n+1):
        res = prev1 + prev2
        prev2 = prev1
        prev1 = res
    return res


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
