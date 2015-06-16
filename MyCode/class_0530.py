__author__ = 'aleh'

class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        #using - makes an object protected
        #self._private








x = Encapsulation(1,2,3)

print x.public
print x._protected
