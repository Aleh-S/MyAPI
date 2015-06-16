__author__ = 'aleh'


class MyCar:
    # classinterface
    def __init__(self, doors=None, color=None):
        #remember this
        if doors is None:
            doors = 2
        if color is None:
            color = 'black'

        #protected data
        _wheels = 4

        print "Our car has %s doors" % (doors)
        print "Out car has %s color\n" % (color)

if __name__ == '__main__':
    car1 = MyCar()
    car2 = MyCar(4,'green')


