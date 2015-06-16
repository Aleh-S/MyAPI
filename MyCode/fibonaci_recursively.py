__author__ = 'aleh'

# 0,1,1,2,3,5,8,13,21


def fib(n):
    l = []

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

print(fib(6))
    



# def fib(n):
#     l = [0]
#     a, b = 0, 1
#     for i in xrange(n):
#         l.append(b)
#         a,b = b, a+b
#     # while b <= n:
#     #     l.append(b)
#     #     a,b = b, a+b
#
#     return l
#
# print fib(8)