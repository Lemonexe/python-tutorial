# CLASS (aka type)
# btw everything is an object, incl. strings numbers etc

type_of_asdf = type('asdf') # gets the class, of which the string 'asdf' is an instance
print(type_of_asdf(8))
print(type_of_asdf([1, 2, 3, 4]))
# what did just happen??? Actually, 'str' is the class of any string - the well-known str function is ctuly class
# so type_of_asdf = str

class Kotatko:
    species = 'ctuly iz a kat'

    # constructor, this one is with optional args
    def __init__(self, *args):
        self.jmeno = args[0] if args else 'bezejmenná kočka'

    def zamnoukej(self): # btw "self" is just a conventional name
        print(f"Mňau já jsem {self.jmeno}, {self.species}")

    def sezrat(self, zradlo):
        print(f"{self.jmeno} sežralo {zradlo}")

    # stringify function - is called whenever the object is treated as a string
    def __str__(self):
        return f"{self.species} called {self.jmeno}"

mourek = Kotatko() # class is capitalized, instance is not capitalized
mourek.zamnoukej()
mourek.jmeno = 'Mourek'
print(f"teď už {mourek.jmeno}")
print('má jméno? ' + str(hasattr(mourek, 'jmeno')))
# mourek.zamnoukej = 12345 # of course I could just overwrite the method with anything

bashka = Kotatko('Bažka') # class is capitalized, instance is not capitalized
bashka.sezrat('rybu') # first param of any method is always self, the other params are callable
bashka.sezrat(zradlo='rybu') # it's better codestyle to explicitly assign the param.

print(bashka, str(bashka))

# NOW LET'S CREATE A ŠTĚŇÁTKO, but to avoid boilerplate it will inherit
class Zviratko:
    def __init__(self, *args):
        self.jmeno = args[0] if args else 'bezejmenné '+self.species
    def sezrat(self, zradlo):
        print(f"{self.jmeno} sežral/a {zradlo}")

# something = Zviratko() # Zviratko is not instantiable like this, it is missing species..

# inheritance is easy like that. Zviratky is superclass, Stenatko is subclass
class Stenatko(Zviratko):
    species = '100% PES'
    def zastekej(self):
        print(f"Haf štěk já jsem {self.jmeno}")

    # superclass already has "sezrat", so override it
    def sezrat(self, zradlo):
        print(f"{self.jmeno} nejdříve {zradlo} očuchává")
        # if we want to extend original fn, just call it now on the superclass
        super().sezrat("očuchané "+zradlo)

zeryk = Stenatko('Žeryk')
zeryk.zastekej()
dog = Stenatko()
dog.sezrat('kost')

# POLYMORPHISM - both Kotatko and Stenatko can be used there where we expect Zviratko
zviratka = [Kotatko('Micka'), Stenatko('Azorek')]
for zviratko in zviratka:
    zviratko.sezrat('flákota')
