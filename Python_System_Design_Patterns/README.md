# Python System Design Patterns
* Important python based system design patterns.


# Pattern Context
* There are 4 important attributes
  1. Participants
     * Classes needed to form a design pattern.
     * Each class has a different role in the design pattern. 
  2. Quality attributes
     * Non-functional system requirements such as:
       * usability
       * modifiability
       * reliability
       * performance
       * ...etc...
     * These effect the ENTIRE SOFTWARE SYSTEM
       * architectural solutions contribute to this.
  3. Forces
     * Various factors or trade-offs to consider in design patterns.
     * These are manifested in quality attributes.
  4. Consequences
     * These occur if forces are not controlled.
     * Bugs and Worse Performance are the most common!
     * Deciding which design pattern(s) to use can prevent unwanted consequences!
    
# Pattern Language
* There are 4 important components of this to consider during system design:
1. Names
   * Capture the "gist" of what it does.
   * Classes and Methods become vocabulary for your system and should be meaningful, memorable, and easy to understand. 
2. Context
   * Scenarios on when to use each pattern.
   * Details insights on when and where each pattern should be used in your system. 
3. Problem
   * This is very important.
   * Describes the design problem or challenge your pattern is handling. 
4. Solution
   * Specifies a pattern thatis being used.
   * Structure describes the relationships.
   * Behavior describes the interactions between pattern elements. 
5. Related Patterns
   * List other patterns or patterns used in tandem.

# Design Pattern Types
1. **Creational**
   * Use
     * Create objects systematically
   * Benefits
     * Flexibility in design and use at run time.
   * **Object Oriented Design**
     * **Polymorphism**
2. **Structural**
   * Use
     * Builds a relationship between software components.
     * Functional AND Non-Functional goals.
  * Benefits
    * Different goals --> different structures
  * **Object Oriented Design**
    * **Inheritance**
3. **Behavioral**
   * Use
     * Object interactions
     * Allows BOTH Functional AND Non-functional goals.
   * Benefits
     * Focus --> Protocols
   * **Object Oriented Design**
     * **Class Methods**
    

# Object Oriented Design
* Design patterns require Object Oriented Programming.

## Objects
* Represent entities in BOTH problem and solution domains.
* Environment -- entities interact with software and environment
* Sofware -- Components within the environment

## Classes
* Templates to create objects.
* Define Attributes and Methods
  1. Attributes
     * Properties of an entity
     * State of an entity
  2. Methods
     * Represent Behaviors of an entity
       * Think of a SQL table in a CRUD system with individual system methods such as:
         * Name
         * Age
         * DOB
         * ...etc..
        
## Inheritance
* Relationships between classes as parent and child.
  1. Child classes
     * Keeps all attributes of parent.
     * Can have its own attributes.
     * Can override methods of parent class.
    
## Polymorphism
* Depends on Inheritance
* Allows child classes to be instantiated and treated as the same type as their parent.
* Enables a parent class to be a "placeholder" for its child classes which often contain specific methods of their own.




# Creational Patterns
1. Factory
   * A factory is an object useful in creating other objects.
   * Especially useful when there are uncertainties in what objects your system actually needs.
   * Decisions can then be made at runtime which classes to implement.
   * Example:
     * You own a pet store that sells Dogs but now you need to add Cats.
    
2. Abstract Factory
   * User expectation is multiple related objects at a given time. 

3. Singleton
   * When you want to allow only 1 object to be created from a class.
   * OOP way of creating global variables.
   * Similar concept called "Borg" exists in python. Borg allows multiple object instances that share the same attribute values --- Borg is short for "Cyborg" from Star Trek.
   * **Why would you need this???**
     * Use Case: Lets say you need to store a cache of information that is shared by multiple objects.
     * If you keep this in 1 single object (singleton) or Borg, you don't have to keep retrieving it each time.
     * All modules in python act as singletons.
    
![image](https://github.com/user-attachments/assets/4209362d-98ce-492b-9b87-04814de3152f)
