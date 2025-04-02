class Borg:
    """The Borg design pattern.
    Makes attributes GLOBAL variables."""
    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # make an attribute dictionary


class Singleton(Borg):
    """The singleton class.
     -- Inherits from Borg Parent Class.
     -- Shares same set of attributes in dictionary."""
    def __init__(self, **kwargs):
        Borg.__init__(self) ## accepts attribute dictionary then updates with new dict item
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data) # Returns attribute dictionary for printing

# Create a singleton object and add first acronym.
def prove_singleton():
    x = Singleton(HTTP = "Hyper Text Transfer Protocol") ## key with string value
    # Print object
    # print(x)
    ## create another singleton object and add another acronym
    y = Singleton(SNMP = "Simple Network Management Protocol") ## dict will add this new acronym
    # Print object
    # print(y)

    return y

result = prove_singleton()
print(result)
