
# Class 2

Lambda Materials:

  + https://learn.lambdaschool.com/ds/module/recqeF16aJfb1UTWF/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module2-oop-code-style-and-reviews

Outline:

  1) Review of Lambdata Package Functionality
  2) Docs, Style, PEP8 and Docstrings
  3) OOP Concepts
  4) Classes and Inheritance in Python

## Part I

Review of functionality for lambdata package - operating on dataframes, converting a column of state abbreviations to state names. Using a functional approach (for now).

Introspection and debugging:

```sh
# introspection:
type("HELLO") # what datatype /class is this object?
dir("HELLO") # method methods and properties are available to be invoked on the object?

# debugging with breakpoint:
for i in [1,2,3,4,5]:
    if i >= 3:
        breakpoint()
```

> NOTE: breakpoint() is available as of Python 3.7 or later. For earlier versions, try `from pdb import set_trace as breakpoint` and then you should be able to use `breakpoint()`.

Branch operations to facilitate Pull Request Reviews:

```sh
git checkout -b my-new-feature # checkout a new branch
git add .
git commit -m "Implement feature"
git push origin my-new-feature
```

## Part II

Style, Formatting, PEP8, and Docstrings:

  + https://pep8.org/
  + https://www.python.org/dev/peps/pep-0008/
  + https://www.python.org/dev/peps/pep-0257/
  + https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
  + https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
  + https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

> The docstring for a function or method should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). Optional arguments should be indicated. It should be documented whether keyword arguments are part of the interface. - PEP 257

Doc generation example (Pandas):

  + https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  + https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py#L319

Doc generation, Read The Docs, Sphinx (BONUS):

  + https://readthedocs.org/
  + https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
  + https://www.youtube.com/watch?v=b4iFyrLQQh4

Style-checking:

  + https://pypi.org/project/autopep8/
  + http://pep8online.com/
  + https://codeclimate.com/

```sh
# use pip or pipenv to install. if pipenv save as dev dependency:
pipenv install autopep8 --dev

# make a commit before running the following command, as the in-place flag will modify your files:
autopep8 --in-place --aggressive --recursive .
```

## Part III

Classes and OOP:

  + https://docs.python.org/3/tutorial/classes.html
  + https://realpython.com/python3-object-oriented-programming/
  + https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
  + https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
  + https://realpython.com/instance-class-and-static-methods-demystified/#static-methods

Characteristics of an "object":

  + Identity
  + Attributes / Properties
  + Behaviors / Methods

Example objects:

![different color polos on the shelf](/img/polos.png)

Example class definition:

```py
# polos.py

class Polo():
    def __init__(self, color, size, price=99.00, style=None):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

if __name__ == "__main__":

    #df = DataFrame(...)
    # df.head()
    polo1 = Polo(color="Blue", size="L", price=4.99) # a new "instance" of the class
    print(polo1.color)
    print(polo1.price)

    polo2 = Polo(color="Yello", size="Small")  # a new "instance" of the class
    print(polo2.color)
    print(polo2.price)
```

> TERMINOLOGY NOTE: the `__init__` function inside a class is often called the "constructor" or "initializer" function

> TERMINOLOGY NOTE: when we create a new instance of the class (e.g. `polo1` and `polo2`, we call this "initialization" or "instantiation"


### Refactoring from a Functional to an Object-Oriented Approach

Example of a functional approach:

```py
# teams.py

def full_name(team_dict):
    return team["city"] + " " + team["name"]

teams = [
    {"name": "Yankees", "city": "New York"},
    {"name": "Mets", "city": "New York"},
    {"name": "Nationals", "city": "Washington"}
]

for team in teams:
    print(full_name(team)) #> functional approach (pass the object to the function)
```

... and converting to an object-oriented approach:

```py
# teams.py

class Team():
    def __init__(self, name, city, sport=None, roster=[]):
        # these are attributes / nouns
        self.name = name
        self.city = city
        self.sport = sport
        self.roster = roster

    # this is a property / noun
    # the @property decorator allows us to invoke this without trailing parentheses
    @property
    def full_name(self):
        return f"{team.city} {team.name}"

    # this is a method / verb
    def advertise(self):
        print("PLEASE COME TO", self.city.upper(), "TO SEE US PLAY")

    # this method doesn't require any information about the specific instance itself
    # the @staticmethod decorator allows us to omit passing "self" as a param
    @staticmethod
    def advertise_generically():
        print("PLEASE COME TO OUR GAMES")

if __name__ == "__main__":

    teams = [
        {"name": "Yankees", "city": "New York"},
        {"name": "Mets", "city": "New York"},
        {"name": "Nationals", "city": "Washington"}
    ]

    for d in teams:
        #print(team["city"] + " " + team["name"])
        #print(full_name(team)) #> functional approach
        team = Team(d["name"], d["city"])
        print(team.name)
        print(team.full_name) #> OOP (invoke the method on the object)
        team.advertise()
```

A real-world example of Refactoring from Functions to Classes (BONUS):
  + https://github.com/s2t2/playlist-service-py/blob/25cae16201adc935f71e863a79d51690c00e492b/app/spotify_service.py
  + https://github.com/s2t2/playlist-service-py/blob/master/app/spotify_service.py
  + https://github.com/s2t2/playlist-service-py/blob/master/app/sync_service.py

## Part IV

Class Inheritance in Python:

  + https://www.w3schools.com/python/python_inheritance.asp

Inheritance Example (SKLearn):

  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L77
  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L589

Starting with a single class:

```py
# autos.py

class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

if __name__ == "__main__":
    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.drive()
    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    truck = Auto("Ford", "F150", 2020, "Blue", 4)
    truck.drive()
    truck2 = Auto("Tesla", "Cybertuck", 2020, "Blue", 4)
    truck2.drive()
```

... then implementing inheritance between classes:

```py
# autos.py

class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)

class Truck(Auto): # designates the Truck class should inherit from the Auto class
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels) # can invoke parent class methods via super()
        self.bed_size = bed_size

    # can overwrite parent class methods
    def advertise(self):
        print("VROOOOM", self.model)

if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.drive()
    car.advertise()

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    car2.advertise()

    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.advertise()
    print(truck.bed_size)

    truck2 = Truck("Tesla", "Cybertuck", 2020, "Blue", 4, bed_size="10x10")
    truck2.drive()
    truck2.advertise()
    print(truck2.bed_size)
```
