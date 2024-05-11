Python assert keyword

Assertions in any programming language are the debugging tools that help in the smooth flow of code. 
Assertions are mainly assumptions that a programmer knows or always wants to be true and hence puts them in code, 
so that failure of these doesn’t allow the code to execute further. 

In simpler terms, we can say that assertion is the boolean expression that checks if the statement is True or False. 
If the statement is true then it does nothing and continues the execution, but if the statement is False then it stops the execution of the program and throws an error.

Let us look at the flowchart of the assertion.

# Example 1: Python assert keyword without error message
# Python 3 code to demonstrate
# working of assert
 
# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0
print(a / b)

#---------------------------

#Example 2: Python assert keyword with error message
# Python 3 code to demonstrate
# working of assert
 
# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Zero Division Error"
print(a / b)

#---------------------------

# Python 3 code to demonstrate
# working of assert
# Application
 
# initializing list of foods temperatures
batch = [ 40, 26, 39, 30, 25, 21]
 
# initializing cut temperature
cut = 26
 
# using assert to check for temperature greater than cut
for i in batch:
    assert i >= 26, "Batch is Rejected"
    print (str(i) + " is O.K" )
    
#---------------------------   

def square(x):
    return x * x

print(square(10) == 100)
assert square(10) == 100

--------------------------

def square(x):
    return x * x


assert square(10) == 101

--------------------------

import math


def is_prime(n):
    """Determines if a non-negative integer is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
-------------------------

tests0.py:

from prime import is_prime


def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")

------------------------

import unittest

from prime import is_prime


class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))


if __name__ == "__main__":
    unittest.main()
    
-----------------------

str() vs repr() in Python

s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))

s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))

Following are differences:

str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable. 
For example, if we suspect a float has a small rounding error, repr will show us while str may not.
repr() compute the “official” string representation of an object (a representation that has all information about the object) 
and str() is used to compute the “informal” string representation of an object (a representation that is useful for printing the object).
The print statement and str() built-in function uses __str__ to display the string representation of the object 
while the repr() built-in function uses __repr__ to display the object.

import datetime
today = datetime.datetime.now()
  
# Prints readable format for date-time object
print (str(today))
  
# prints the official format of date-time object
print (repr(today))  

# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes
  
# A user defined class to represent Complex numbers
class Complex:
  
    # Constructor
    def __init__(self, real, imag):
       self.real = real
       self.imag = imag
  
    # For call to repr(). Prints object's information
    def __repr__(self):
       return 'Rational(%s, %s)' % (self.real, self.imag)    
  
    # For call to str(). Prints readable form
    def __str__(self):
       return '%s + i%s' % (self.real, self.imag)    
  
  
# Driver program to test above
t = Complex(10, 20)
  
# Same as "print t"
print (str(t))  
print (repr(t))

#---------------------------------------

class Square:
    def __init__(self, side):
        """ creates a square having the given side
        """
        self.side = side
  
    def area(self):
        """ returns area of the square
        """
        return self.side**2
  
    def perimeter(self):
        """ returns perimeter of the square
        """
        return 4 * self.side
  
    def __repr__(self):
        """ declares how a Square object should be printed
        """
        s = 'Square with side = ' + str(self.side) + '\n' + \
        'Area = ' + str(self.area()) + '\n' + \
        'Perimeter = ' + str(self.perimeter())
        return s
  
  
if __name__ == '__main__':
    # read input from the user
    side = int(input('enter the side length to create a Square: '))
      
    # create a square with the provided side
    square = Square(side)
  
    # print the created square
    print(square)
    
#-----------------------------------------

from Test1 import Square
import unittest
  
class TestSum(unittest.TestCase):
  
    def test_area(self):
        sq = Square(2)
  
        self.assertEqual(sq.area(), 4, 
            f'Area is shown {sq.area()} rather than 9')
  
if __name__ == '__main__':
    unittest.main()
    
#-----------------------------------------

Now, let’s write some tests for our small software discussed above using the unittest module.

    Create a file named tests.py in the folder named “tests”.
    In tests.py import unittest.
    Create a class named TestClass which inherits from the class unittest.TestCase.

    Rule 1: All the tests are written as the methods of a class, which must inherit from the class unittest.TestCase.
    Create a test method as shown below.
    Rule 2: Name of each and every test method should start with “test” otherwise it’ll be skipped by the test runner.
    Rule 3: We use special assertEqual() statements instead of the built-in assert statements available in Python.

The first argument of assertEqual() is the actual output, the second argument is the desired output 
and the third argument is the error message which would be displayed in case the two values differ from each other (test fails).

#------------------------------------

What is Unit Testing?
Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. 
This is used to validate that each unit of the software performs as designed.

OOP concepts supported by unittest framework:

    test fixture:
    A test fixture is used as a baseline for running tests to ensure that there is a fixed environment in which tests are run so that results are repeatable.
    Examples :
        creating temporary databases.
        starting a server process.
    test case:
    A test case is a set of conditions which is used to determine whether a system under test works correctly.
    test suite:
    Test suite is a collection of testcases that are used to test a software program to show that it has some specified set of behaviours by executing the aggregated tests together.
    test runner:
    A test runner is a component which set up the execution of tests and provides the outcome to the user.
    
Outcomes Possible :
There are three types of possible test outcomes :

    OK – This means that all the tests are passed.
    FAIL – This means that the test did not pass and an AssertionError exception is raised.
    ERROR – This means that the test raises an exception other than AssertionError.
    
#-----------------------------------------

The above code is a short script to test 5 string methods. unittest.TestCase is used to create test cases by subclassing it. The last block of the code at the bottom allows us to run all the tests just by running the file.

Basic terms used in the code :

    assertEqual() – This statement is used to check if the result obtained is equal to the expected result.
    assertTrue() / assertFalse() – This statement is used to verify if a given statement is true or false.
    assertRaises() – This statement is used to raise a specific exception.

Description of tests :

    test_strings_a
    This test is used to test the property of string in which a character say ‘a’ multiplied by a number say ‘x’ gives the output as x times ‘a’. The assertEqual() statement returns true in this case if the result matches the given output.
    test_upper
    This test is used to check if the given string is converted to uppercase or not. The assertEqual() statement returns true if the string returned is in uppercase.
    test_isupper
    This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. The assertTrue() / assertFalse() statement is used for this verification.
    test_strip
    This test is used to check if all chars passed in the function have been stripped from the string. The assertEqual() statement returns true if the string is stripped and matches the given output.
    test_split
    This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. The assertEqual() statement returns true in this case if the result matches the given output.

unittest.main() provides a command-line interface to the test script.On running the above script from the command line, following output is produced :

import unittest
  
class SimpleTest(unittest.TestCase):
  
    # Returns True or False. 
    def test(self):        
        self.assertTrue(True)
  
if __name__ == '__main__':
    unittest.main()
    
#---------------------

# Python code to demonstrate working of unittest
import unittest
  
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual( 'a'*4, 'aaaa')
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')
  
    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
  
    # Returns true if the string is stripped and 
    # matches the given output.
    def test_strip(self):        
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')
  
    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
  
if __name__ == '__main__':
    unittest.main()
    
#-------------------------------

# test suite
import unittest
  
  
class TestStringMethods(unittest.TestCase):
    # test function to test whether key is present in container
    def test_positive(self):
        key = "geeks"
        container = "geeksforgeeks"
        # error message in case if test case got failed
        message = "key is not in container."
        # assertIn() to check if key is in container
        self.assertIn(key, container, message)
  
  
if __name__ == '__main__':
    unittest.main()
    
#---------------------------------


---------------------------

# pip install pytest
import unittest
from Test1 import Square

def test_file1_area():
    sq = Square(2)
    assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()}"
  
def test_file1_perimeter():
    sq = Square(-1)
    assert sq.perimeter() == -1, f'perimeter is shown {sq.perimeter()} rather than -1'

# pokretanje iz konzole: py.test PyTest1.py

# testiranje samo metode perimeter
# py.test PyTest1.py -k "perimeter" 

---------------------------

test1.py

# pip install pytest
import unittest
from Test1 import Square

def test_file1_area():
    sq = Square(2)
    assert sq.area() == 4, f"area for side {sq.side} units is {sq.area()}"
  
def test_file1_perimeter():
    sq = Square(-1)
    assert sq.perimeter() == -1, f'perimeter is shown {sq.perimeter()} rather than -1'

# py.test test_1.py

-----------------------

import unittest

# Defining a TestCase Subclass
def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

# python -m unittest test_add_fish_to_aquarium.py

# py.test test_add_fish_to_aquarium.py

'''
Note: TestCase recognizes test methods as any method that begins with test. 
For example, def test_add_fish_to_aquarium_success(self) is recognized as a test and will be run as such. def example_test(self), 
conversely, would not be recognized as a test because it does not begin with test. 
Only methods beginning with test will be run and reported when you run python -m unittest ....
'''

# u drugoj funkciji promeniti: expected = {"tank_a": ["rabbit"]} i ponovo testirati

--------------------------

import unittest

# Defining a TestCase Subclass
def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_exception(self):
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(
            str(exception_context.exception),
            "A maximum of 10 fish can be added to the aquarium"
        )

# python -m unittest test_add_fish_to_aquarium.py

# py.test test_add_fish_to_aquarium.py

'''
Note: TestCase recognizes test methods as any method that begins with test. 
For example, def test_add_fish_to_aquarium_success(self) is recognized as a test and will be run as such. def example_test(self), 
conversely, would not be recognized as a test because it does not begin with test. 
Only methods beginning with test will be run and reported when you run python -m unittest ....
'''

# u drugoj funkciji promeniti: expected = {"tank_a": ["rabbit"]} i ponovo testirati

----------------------------

import unittest

class FishTank:
    def __init__(self):
        self.has_water = False

    def fill_with_water(self):
        self.has_water = True

class TestFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = FishTank()

    def test_fish_tank_empty_by_default(self):
        self.assertFalse(self.fish_tank.has_water)

    def test_fish_tank_can_be_filled(self):
        self.fish_tank.fill_with_water()
        self.assertTrue(self.fish_tank.has_water)

#  python -m unittest test_fish_tank.py

'''
TestCase also supports a setUp method to help you create resources on a per-test basis. 
setUp methods can be helpful when you have a common set of preparation code that you want to run before each and every one of your tests. 
setUp lets you put all this preparation code in a single place, instead of repeating it over and over for each individual test.
'''

-------------------------

import os
import unittest

class AdvancedFishTank:
    def __init__(self):
        self.fish_tank_file_name = "fish_tank.txt"
        default_contents = "shark, tuna"
        with open(self.fish_tank_file_name, "w") as f:
            f.write(default_contents)

    def empty_tank(self):
        os.remove(self.fish_tank_file_name)


class TestAdvancedFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = AdvancedFishTank()

    def tearDown(self):
        self.fish_tank.empty_tank()

    def test_fish_tank_writes_file(self):
        with open(self.fish_tank.fish_tank_file_name) as f:
            contents = f.read()
        self.assertEqual(contents, "shark, tuna")

'''
Using the tearDown Method to Clean Up Resources

TestCase supports a counterpart to the setUp method named tearDown. 
tearDown is useful if, for example, we need to clean up connections to a database, 
or modifications made to a filesystem after each test completes. 
We’ll review an example that uses tearDown with filesystems:
'''

#test_advanced_fish_tank.py

------------------------

import unittest
  
class SimpleTest(unittest.TestCase):
  
    # Returns True or False. 
    def test(self):        
        self.assertTrue(True)
  
if __name__ == '__main__':
    unittest.main()
    
-----------------------

# Python code to demonstrate working of unittest
import unittest
  
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual( 'a'*4, 'aaaa')
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')
  
    # Returns TRUE if the string is in uppercase
    # else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
  
    # Returns true if the string is stripped and 
    # matches the given output.
    def test_strip(self):        
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')
  
    # Returns true if the string splits and matches
    # the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
  
if __name__ == '__main__':
    unittest.main()
    
---------------------

# test suite
import unittest
  
  
class TestStringMethods(unittest.TestCase):
    # test function to test whether key is present in container
    def test_positive(self):
        key = "geeks"
        container = "geeksforgeeks"
        # error message in case if test case got failed
        message = "key is not in container."
        # assertIn() to check if key is in container
        self.assertIn(key, container, message)
  
  
if __name__ == '__main__':
    unittest.main()
    
-----------------

# test suite
import unittest
  
class TestStringMethods(unittest.TestCase):
    
    # negative test function to test if values1 is less or equal than value2
    def test_negativeForLessEqual(self):
        first = 6
        second = 5
          
        # error message in case if test case got failed
        message = "first value is not less than or equal to second value."
          
        # assert function() to check if values1 is less or equal than value2
        self.assertLessEqual(first, second, message)
  
if __name__ == '__main__':
    unittest.main()
    
----------------------

# unit test case
import unittest
  
class DummyClass:
  x = 5
  
class TestMethods(unittest.TestCase):
    # test function to test object equality of two value
    def test_negative(self):
        firstValue = DummyClass()
        secondValue = DummyClass()
        # error message in case if test case got failed
        message = "First value & second value are not evaluated to same object !"
        # assertIs() to check that if first & second evaluated to same object
        self.assertIs(firstValue, secondValue, message)
  
if __name__ == '__main__':
    unittest.main()
    
-----------------------

# unit test case
import unittest
  
class DummyClass:
  x = 5
  
class TestMethods(unittest.TestCase):
    # test function to test object equality of two value
    def test_positive(self):
        firstValue = DummyClass()
        secondValue = firstValue
        # error message in case if test case got failed
        message = "First value and second value are not evaluated to same object !"
        # assertIs() to check that if first & second evaluated to same object
        self.assertIs(firstValue, secondValue, message)
  
if __name__ == '__main__':
    unittest.main()