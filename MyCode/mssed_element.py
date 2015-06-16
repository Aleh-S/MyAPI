__author__ = 'aleh'

# variant 1
# def missed_num(list1):
#     for i in range(len(list1)-1):
#         if list[i+1]-list[i] != 1:
#             return "missing number after: %s" % list[i]
#     return 'OK'
#
#
# list = [0,1,2,4,5]
# print missed_num(list)

from random import randint
def missed_num(l):
    sum_l = 0
    sum_l2 = 0

    l2 = list(range(min(l), max(l)+1))

    for i in l:
        sum_l += 1
    for j in l2:
        sum_l2 += 1

    return sum_l2 - sum_l


list1 = [0,1,2,4,5]
print missed_num(list1)