

def test(foo):
    print(list(map(foo, range(10))))

def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2) 

test(fib)

def fib_lin(n: int) -> int:
    if n < 2:
        return 1
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

test(fib_lin)


def fib_log(n: int) -> int:
    if n < 2:
        return 1

    def matmul(m1, m2):
        return (
                m1[0]*m2[0] + m1[1]*m2[2],
                m1[0]*m2[1] + m1[1]*m2[3],
                m1[2]*m2[0] + m1[3]*m2[2],
                m1[2]*m2[1] + m1[3]*m2[3]
                )
    mat = (1, 0, 0, 1)
    powmat = (1, 1, 1, 0)
    while n > 0:
        if n%2 == 1:
            mat = matmul(mat, powmat)
        powmat = matmul(powmat, powmat)
        n //= 2

    return mat[0]

test(fib_log)
