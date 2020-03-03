from abc import abstractmethod

class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

    # Now we're going to create the first subclass

class Owl(Bird):

        def reproduce(self):
            self.babies += 6

        def eat(self):
            print("Peck Peck")

# Here Polymorphism is used to override reproduce method
# Abstraction with the eat method and
# Inheritance in this child class.

#Now we'll add another subclass

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        print("Nom Nom")

    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            print("No more dodo's")

# For this subclass Polymorphism overrides method and
# Fly and extinct variables.
# Encapsulation to keep the babies variable being
# accessed as well as Ingeritance again to
# create a child class of Bird

