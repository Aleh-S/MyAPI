__author__ = 'aleh'
from random import randint

def generate_int():
    return [randint(0,9)for i in range(4)]


def user_input():

    x = raw_input('Please enter 4 digit number:\n')

    if len(x) == 4:

        try:
            list1 = [int(i) for i in str(x)[0:4]]
            return list1
        except ValueError:
            print ('Please try again')
            user_input()
    else:
        print('Please enter 4 digit number')
        user_input()



def cows_bulls(l1, l2):
    cows = 0
    bulls = 0

    for i in range(4):
        if l1[i] == l2[i]:
            bulls += 1

            l1[i] = None
            l2[i] = None
    for i in l1:
        for j in l2:
            if i == j and i and j:
                cows += 1


    #return cows, bulls
    print 'Cows: %s, Bulls: %s ' % (cows, bulls)



cows_bulls(user_input(), generate_int())






