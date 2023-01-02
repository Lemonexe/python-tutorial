# CONSTRUCTOR
class Singleton:
    # special function, like the well-known __init__ BUT THIS IS DIFFERENT
    # __init__ does not rly create the object, it gets it already created as "self" and does stuff on it
    def __new__(cls):
        try:
            print('I\'m trying to access the already existing instance')
            return cls._instance # this is the creation
        except AttributeError:
            print('but it didn\'t exist yet, have to create it.')
            cls._instance = super().__new__(cls)
            return cls._instance

obj = Singleton()
obj2 = Singleton()
print(f"\nare obj & obj2 actually THE SAME INSTANCE? {obj is obj2}")

# practical example:
a = tuple((3, 4)) # how about it takes two arguments instead of tuple, to create a tuple?
class Bod(tuple): # inherit from tuple
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

b = Bod(3, 4)
print('\n', a, b)
