class parent:
    def __init__(self, value):
        self.value = value

    def google(self):
        print(f'executing parent Google {self.value}')

    def apple(self):
        print('executing parent Apple')
        self.google()

''' # this makes use of all the contets in the parent class. constructor, instance methods etc'''

# child class having a separate method
class child(parent):

    def demo(self):
        print('Executing demo')

# child overriding/ redefining parent class method


''' ANYTHING WE ACCESS BY USING A DOT OPERATOR IS CALLED A ATTRIBUTE '''


class child2(parent):

    def hello(self):
        print('hello world')

    def google(self):
        print(f'executing child2 google {self.value}')


''' * method resolution order .__mro__ will give us the attributes in the class '''

# child adding extra functionality and reusing the original functionality of parent


class child3(parent):

    def google(self):
        print('Executing child3 google !!', self.value)
        super().google()


""" super() function is used to cal the parent class 'attributes' """


# child class having an extra attribute


class child4(parent):
    def __init__(self, value, name):
        self.name = name
        super().__init__(value)  # calling parent class constructor


class facebook:
    def spam(self):
        print('executing facebook spam')

# child inheriting from multiple parents


class child5(parent, facebook):
    pass

# multi level inheritence


class a:
    def demo(self):
        print('executing a')


class b(a):
    def demo(self):
        print('executing b')
        super(b, self).demo()



class c(b):
    def demo(self):
        print('executing c')
        super(c, self).demo()


A = c()
A.demo()

# multiple inheritance

