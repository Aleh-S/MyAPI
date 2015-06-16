
from random import randint

l = [randint(0,20) for i in range(10)]
print l
m = dict()
for i in l:
    if i not in m:
        m[i] = 1
        print m
    else:
        m[i] +=1
        print m
for j in m:
    if m[j] == 1:
        print 'Number %s is unique' % str(j)
    else:
        print "Number %s is not unique" % str(j)
