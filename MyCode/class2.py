__author__ = 'aleh'

class MyClass():
    # default property
    prop1 = "I am a class property!"

    # method which sets a new property

    def setProperty(self, newval):
        self.prop1 = newval

    # method which sets a new property

    def getProperty(self):
        return self.prop1


obj = MyClass()
print(obj.prop1)
obj.setProperty("I'm a new property value!")
print(obj.getProperty())

obj2 = MyClass()
obj2.setProperty('The Newest property')
print(obj2.getProperty())

print obj2

