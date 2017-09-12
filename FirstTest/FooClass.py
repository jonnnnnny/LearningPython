class FooClass(object):
    version = 0.1

    def __init__(self, name='jonny'):
        self.name = name
        print("Created a class instance for", name)
    def showName(self):
        print("your name is ", self.name)
        print("My name is ", self.__class__.__name__)
    def showVer(self):
        print(self.version)
    def addM2M(self, x):
        return x+x



fool = FooClass()

fool.showVer()
fool.showName()
