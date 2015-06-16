def fib(n):
    l = [0]
    a, b = 0, 1


   # to make fibonachi of n numbers
    # for i in xrange(n):
    #     l.append(b)
    #     a,b = b, a+b


   # to make fibonachi to stop at n number
    while b <= n+2:
        l.append(b)
        a,b = b, a+b

    return l

print fib(8)