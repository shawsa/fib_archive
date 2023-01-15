from itertools import islice
from more_itertools import iterate, nth
from functools import partial

def test10(foo):
    return list(map(foo, range(10)))

implementations = {}
def register(foo):
    implementations[foo.__name__] = foo
    return foo

@register
def fib_naive(n: int) -> int:
    if n < 2:
        return n
    return fib_naive(n-1) + fib_naive(n-2) 

@register
def fib_lin(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

@register
def fib_lin_functional(n: int):
    def fib_iteration(tup):
        a, b = tup
        return b, a+b

    second = partial(nth, n=1)

    def fib_seq():
        yield 0
        yield from map(second,
                       iterate(fib_iteration, (0, 1)))

    return nth(fib_seq(), n)

@register
def fib_log(n: int) -> int:
    if n < 2:
        return n

    def matmul(m1, m2):
        return (
                m1[0]*m2[0] + m1[1]*m2[2],
                m1[0]*m2[1] + m1[1]*m2[3],
                m1[2]*m2[0] + m1[3]*m2[2],
                m1[2]*m2[1] + m1[3]*m2[3]
                )

    def mat_vec_mul(m, v):
        return (m[0]*v[0] + m[1]*v[1], m[2]*v[0] + m[3]*v[1])

    vec = (1, 0)
    powmat = (1, 1, 1, 0)
    n -= 1  # one fewer steps to take than terms in the sequence.
    while n > 0:
        if n%2 == 1:
            vec = mat_vec_mul(powmat, vec)
        powmat = matmul(powmat, powmat)
        n //= 2

    return vec[0]


if __name__ == '__main__':
    max_len = max(map(len, implementations.keys()))
    for name, foo in implementations.items():
        print(f'{foo.__name__.rjust(max_len)}: {test10(foo)}')
