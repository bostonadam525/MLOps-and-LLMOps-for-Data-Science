## Prototype pattern
import copy

class Prototype:

    def __init__(self):
        ## create dict object
        self._objects = {}

    ## takes in name, object to be cloned
    def register_object(self, name, obj):
        """Register an object."""
        self._objects[name] = obj ## stores key name with object to be cloned

    ## deletes methods from dictionary
    def unregister_object(self, name):
        """Unregister an object."""
        del self._objects[name] # delete object by its key which is name

    ## clones prototypical object
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes."""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

## define prototype object we are cloning
class Car:
    def __init__(self):
        ## init attributes with default values
        self.name = "SkyLark"
        self.color = "Red"
        self.options = "Ex"

    ## return strings for printing
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


## init objects to be cloned
c = Car()
prototype = Prototype()
prototype.register_object('skylark', c)

## clone prototype object
c1 = prototype.clone('skylark')

## print cloned object
print(c1)
