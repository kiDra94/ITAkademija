Funkcija koja računa maksimum dva broja:

def maxi0(a, b):
    if a > b:
        return a
    else:
        return b
        
print(maxi0(3, 7))

---

Ili preko ternarnog operatora:

def maxi(a, b):
    return a if a > b else b

print(maxi(3, 7))

---

Ili preko lambda funkcije:

Max = lambda a, b : a if(a > b) else b
print(Max(3, 7))


---

Funkcija koja računa maksimum tri broja:

def maxi1(a, b, c):
    if a > c:
        if a > b:
            return a
        else:
            return b
    else:
        if c > b:
            return c
        else:
            return b


print(maxi1(9, 7, 5))

---

Ili kombinovano sa ternarnim operatorom:

def maxi2(a, b, c):
    if a > c:
        return a if a > b else b
    else:
        return c if c > b else b


print(maxi2(9, 7, 5))

---

Ili samo preko ternarnog operatora

def maxi3(a, b, c):
    return a if a > b else b if a > c else c if c > b else b


print(maxi3(9, 17, 5))

---

Ili preko ugrađene funkcije max za proizvoljan broj argumenata

print(max(17,9,5))

print(max(5, 3, 4, 8, 9, 11, 23, 12, 4))

---

Potencijalne implementacije ugradjene funkcije max

def maxi4(*arg: int) -> int:
    m: int = arg[0]
    for i in range(1, len(arg)):
        if arg[i] > m:
            m = arg[i]
    return m

print(maxi4(5, 3, 4, 8, 9, 11, 23, 12, 4))

def maxi5(*arg: int) -> int:
    m: int = arg[0]
    for i in arg[1:]:
        if i > m:
            m = i
    return m

print(maxi5(5, 3, 4, 8, 9, 11, 23, 12, 4))

---

Demonstrirati rad sa proizvoljnim brojem argumenata

def fun(*arg):
    print(type(arg))
    print(arg)
    print(*arg)
    print(arg[0])
    print(type(arg[0]))
    print(arg[1:])
    print(*arg[1:])

fun(5, 3, 4, 8, 9, 11, 23, 12, 4)


<class 'tuple'>
(5, 3, 4, 8, 9, 11, 23, 12, 4)
5 3 4 8 9 11 23 12 4
5
<class 'int'>
(3, 4, 8, 9, 11, 23, 12, 4)
3 4 8 9 11 23 12 4

---

Rekurzivna implementacija funkcije max

from typing import List, Tuple

def max_rek(*arg: Tuple[int]) -> int:
    if len(arg) == 1:
        return arg[0]
    pom = max_rek(*arg[1:])
    return arg[0] if arg[0] > pom else pom

print(max_rek3(5, 3, 4, 8, 9, 11, 23, 12, 4))

---

Ili rekurzivno uz korišćenje funkcije max samo za dva argumenta

def max_rek2(*arg: Tuple[int]) -> int:
    if len(arg) == 1:
        return arg[0]
    return max(arg[0],max_rek2(*arg[1:]))


print(max_rek2(5, 3, 4, 8, 9, 11, 23, 12, 4))

def max_rek3(arg: List[int]) -> int:
    if len(arg) == 1:
        return arg[0]
    return max(arg[0],max_rek3(arg[1:]))


print(max_rek3([5, 3, 4, 8, 9, 11, 23, 12, 4]))

-------------------------------------------------------------------------------

Suma proizvoljnog broja unetih argumenata:

def suma_iter(*a):
    suma = 0
    for i in a:
        suma+=i
    return suma

print(suma_iter(7,4,1,9,8))

def suma(*a):
    if len(a)==1:
        return a[0]
    return a[0] + suma(*a[1:])

print(suma(7,4,1,9,8))

---

Suma elemenata u listi (list) ili torci (tuple):

def suma_iter(a):
    suma = 0
    for i in a:
        suma+=i
    return suma

print(suma_iter([7,4,1,9,8]))
print(suma_iter((7,4,1,9,8)))

---

def suma(a):
    if len(a)==1:
        return a[0]
    return a[0] + suma(a[1:])

print(suma([7,4,1,9,8]))
print(suma((7,4,1,9,8)))

---

Sumiranje preko ugradjene funkcije sum:

print(sum([7,4,1,9,8]))
print(sum((7,4,1,9,8)))

my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print(total)

---

my_set = {1, 2, 3, 4, 5}
total = sum(my_set)
print(total) 

---

Sumiranje sa početnom vrednoscu 0:

numbers = [1,2,3,4,5,1,4,5]
 
Sum = sum(numbers)
print(Sum)

Sumiranje sa početnom vrednoscu 10:
 
Sum = sum(numbers, 10)
print(Sum)

---

Aritmetička sredina članova niza

numbers = [1,2,3,4,5,1,4,5]

def average(numb):
    return sum(numbers)/len(numbers) 
    
print(average(numbers))


--------------------------------------------------------------------------------


Create a function with three parameters a, b and c. The function calculates the quadratic equation:

from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:
    result = None
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        result = (-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        result = -b / (2 * a),
    print(result)

    return result

if __name__ == "__main__":
    assert solution(1, 6, 5) == (-5, -1)
    assert solution(1, 4, 4) == (-2,)
    assert solution(1, 6, 45) is None
    
--------------------------------------------------------------------------------

Create a function with two parameters a and b. The function calculates the following expression:

(12 * a + 25 * b) / (1 + a**(2**b))	

and returns a result of the expression rounded up to the second decimal place.

from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  result = round((12 * a + 25 * b) / (1 + a**(2**b)),2)
  print(result)
  return result

if __name__ == "__main__":
    assert some_expression_with_rounding(2, 3) == 0.39
    assert some_expression_with_rounding(0, 0) == 0.00
    
--------------------------------------------------------------------------------

Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result.

For example:

>>> a_b = '1/3'
>>> c_b = '5/3'
>>> get_fractions(a_b, c_b)
'1/3 + 5/3 = 6/3'

def get_fractions(a_b: str, c_b: str) -> str:
    (n1, d1) = a_b.split("/")
    (n2, d2) = c_b.split("/")
    rez = str(int(n1)+int(n2))+"/"+d2
    return f"{a_b} + {c_b} = {rez}"

if __name__ == "__main__":
    assert get_fractions('1/3','5/3') == '1/3 + 5/3 = 6/3'
    assert get_fractions('1/13','5/13') == '1/13 + 5/13 = 6/13'
    assert get_fractions('23/65','11/65') == '23/65 + 11/65 = 34/65'


--------------------------------------------------------------------------------

Kreirati klasu za rad sa nizovima

class Array(object):
    ''' sizeOfArray: denotes the total size of the array to be initialized
       arrayType: denotes the data type of the array(as all the elements of the array have same data type)
       arrayItems: values at each position of array
    '''

    def __init__(self, sizeOfArray, arrayType=int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)] * sizeOfArray  # initialize array with zeroes
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    # magic methods to enable indexing
    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if self.arrayItems[i] == keyToSearch:  # brute-forcing
                return i  # index at which element/ key was found

        return -1  # if key not found, return -1

    # function for inserting an element
    def insert(self, keyToInsert, position):
        if self.sizeOfArray > position:
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)

    # function to delete an element
    def delete(self, position):
        if self.sizeOfArray > position:
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
        else:
            print('Array size is:', self.sizeOfArray)


if __name__ == '__main__':
    a = Array(10, int)
    print(a)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4, 7)
    print(len(a))
    print(a)
    a.delete(1)
    print(a)
    print(a[2])
    a[3] = 7
    print(a)
    
------------------------------------------------------------------------------

Kreirati funkciju koja "obrće" niz

import Arrays


def reversingAnArray(start, end, myArray):
    while (start < end):
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    myArray = Arrays.Array(10)
    myArray.insert(2, 2)
    myArray.insert(1, 3)
    myArray.insert(3, 1)
    print('Array before Reversing:', myArray)
    reversingAnArray(0, len(myArray), myArray)
    print('Array after Reversing:', myArray)
    
    print(myArray[::-1])
    print(myArray[::-1][::-1])

------------------------------------------------------------

Zarotirati niz za zadati broj mesta (rotateby):

from Arrays import Array


def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray


def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:', myArray)
    print('After Rotation:', rotation(3, myArray))

---------------------------------------------------------------


# Given an array of positive integers. All numbers occur even number of times except one
# number which occurs odd number of times. Find the number in O(n) time & constant space.

# XOR of all elements gives us odd occurring element. Please note that XOR of two elements
# is 0 if both elements are same and XOR of a number x with 0 is x.

# NOTE: This will only work when there is only one number with odd number of occurences.

def printOddOccurences(array):
    odd = 0

    for element in array:
        # XOR with the odd number
        odd = odd ^ element

    return odd

if __name__ == '__main__':
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(printOddOccurences(myArray))      # 4
    
----------------------------------------------------------------------

Implementirati algoritam brzog sortiranja (Quicksort)

def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)


a = [3, 2, 5, 7, 4, 1, 9, 8, 0, 7]
print(quickSort(a))

----------------------------------------------------------------------

# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose sum is exactly x.

def checkSum(array, sum):
    # sort the array in ascending order
    # new changes : made use of Python's inbuilt Merge Sort method
    # Reason for such change : Worst case Time complexity of Quick Sort is O(n^2) whereas Worst Case Complexity of Merge Sort is O(nlog(n))
    array = sorted(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex] ==  sum):
            return array[leftIndex], array[rightIndex]
        elif(array[leftIndex] + array[rightIndex] < sum):
            leftIndex += 1
        else:
            rightIndex += 1

    return False, False


if __name__ == '__main__':
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    number1, number2 = checkSum(myArray, sum)
    if(number1 and number2):
        print('Array has elements:', number1, 'and', number2, 'with sum:', sum)
    else:
        print('Array doesn\'t have elements with the sum:', sum)

Napomena: za prethodni problem može se iskoristiti i program za generisanje permutacija (tj. program za popunjavanja ranca)

def perm(a, s, k):
    if sum(s) == k and len(s) == 2:
        print(s)
        return 
    for i in range(len(a)):
        s.append(a[i])
        perm(a[:i] + a[i + 1:], s.copy(), k)
        s = s[:-1]  # brisanje dodatog elementa pre rekurzivnog poziva 

a = [3, 2, 5, 4]
k = 7
perm(a, [], k)

--------------------------------------------------------------------------

Pronaći dužinu najdužeg opadajućeg podniza niza arr do pozicije n

def lds(arr, n):
    lds = [0] * n
    max = 0

    # Initialize LDS with 1 for all index 
    # The minimum LDS starting with any 
    # element is always 1 
    for i in range(n):
        lds[i] = 1

    # Compute LDS from every index 
    # in bottom up manner 
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    # Select the maximum  
    # of all the LDS values 
    for i in range(n):
        if (max < lds[i]):
            max = lds[i]

            # returns the length of the LDS 
    return max


print(lds([1, 3, 2, 1, 5, 4, 2, 0, 3, 4], 7))
# 3
print(lds([1, 3, 2, 1, 5, 4, 2, 0, 3, 4], 8))
# 4

Napomena: problem može se rešiti preko jedne petlje (linearno vreme)

def lds(a, n):
    pom = maxx = 1
    for i in range(len(a[:n])-1):
        pom = pom + 1 if a[i] > a[i + 1] else 1
        maxx = max(maxx, pom)
    return maxx


print(lds([1, 3, 2, 1, 5, 4, 2, 0, -1, 5, 4], 7))
# 3
print(lds([1, 3, 2, 1, 5, 4, 2, 0, -1, 5, 4], 8))
# 4
print(lds([1, 3, 2, 1, 5, 4, 2, 0, -1, 5, 4], 9))
# 5

----------------------------------------------------------------------

Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string. 
The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on). 
If there are multiple longest words in the string with the same length return the word that occurs first.

Example:

>>> get_longest_word('Python is simple and effective!')
'effective!'
    
def get_longest_word(s: str) -> str:
    rec = ""
    duz = 0
    maxRec = 0
    maxDuz = 0
    for i in s:
        if(i!=' '):
            rec+=i
            duz = duz + 1
            if(duz>maxDuz):
                maxDuz = duz
                maxRec = rec
        else:
            rec = ""
            duz = 0
    return maxRec

print(get_longest_word('Python is simple and effective!'))

---

def get_longest_word2(s: str) -> str:
    max = 0
    najveca = ''
    for i in s.split():
        if(len(i)>max):
            max = len(i)
            najveca = i
    return najveca

print(get_longest_word2('Python is simple and effective!'))

---

def get_longest_length(s: str) -> str:
    return max(map(len,s.split()))

print(get_longest_length('Python is simple and effective!'))

--------------------------------------------------------------------------------

Implement a function that receives a string and replaces all " symbols with ' and vice versa.

def replacer(s: str) -> str:
    string = ""
    for i in s:
        if (i == "\""):
            string += '\''
        elif (i == "\'"):
            string += "\""
        else:
            string += i
    return string
    
first_string = "This is \"double quotes\" in double quotes"
print(replacer(first_string))
    
--------------------------------------------------------------------------------

Write a function that checks whether a string is a palindrome or not. The usage of any reversing functions is prohibited.

To check your implementation you can use strings from here

Examples:

A dog! A panic in a pagoda!
Do nine men Interpret? Nine men I nod
T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet.
A man, a plan, a canal — Panama!
    
def check_str(s: str)->bool:
    res = ""
    for char in s:
        if char.isalpha() or char.isdigit():
            res += char
    res = res.lower()
    for i in range(len(res)//2):
        if(res[i]!=res[len(res)-i-1]):
            return False
    return True
    
str1="A dog! A panic in a pagoda!"
str2="Do nine men Interpret? Nine men I nod"
str3="T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet."
str4="A man, a plan, a canal — Panama!"
str5="32635745"

def palindrom(s:str)->bool:
    res = ""
    for char in s:
        if char.isalpha() or char.isdigit():
            res += char
    res = res.lower()
    print(res)
    for i in range(len(res)//2):
        if(res[i]!=res[len(res)-i-1]):
            return False
    return True

print(palindrom(str1))
print(palindrom(str2))
print(palindrom(str3))
print(palindrom(str4))
print(palindrom(str5))

---

def proveri_pal(s: str) -> bool:
    return s == s[::-1]

print(proveri_pal("AnaVolimilovana".lower()))

--------------------------------------------------------------------------------

Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form.

Examples:

Input:

('red', 'white', 'black', 'red', 'green', 'black') 
Output:

['black', 'green', 'red', 'white']

from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    lista = []
    for i in str_list:
        if i not in lista:
            lista.append(i)
    lista.sort()
    return lista # ne bi moglo return lista.sort()

print(sort_unique_elements((7,7,2,3,3)))
print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))

---

def sort_unique_elements2(str_list: Tuple[str]) -> List[str]:
    return set(i for i in str_list)

print(sort_unique_elements2((7,7,2,3,3)))
print(sort_unique_elements2(('red', 'white', 'black', 'red', 'green', 'black')))

--------------------------------------------------------------------------------

Update the get_fizzbuzz_list function. The function has to generate and return a list with numbers from 1 to n inclusive where the n is passed as a parameter to the function. 
But if the number is divided by 3 the function puts a Fizz word into the list, and if the number is divided by 5 the function puts a Buzz word into the list. 
If the number is divided by both 3 and 5 the function puts FizzBuzz into the list.

from typing import Union, List

ListType = List[Union[int, str]]

def get_fizzbuzz_list(n: int) -> ListType:
    lista = [i for i in range(1,n+1)]
    for i in lista:
        if(i%15==0):
            lista[i-1] = "FizzBuzz"
        elif(i%3==0):
                lista[i-1] = "Fizz"
        elif(i%5==0):
                lista[i-1] = "Buzz"
    #print(lista)
    return lista

print(get_fizzbuzz_list(35))
    
--------------------------------------------------------------------------------

Implement a function foo(List[int]) -> List[int] which, given a list of integers, 
returns a new list such that each element at index i of the new list is the product of all the numbers in the original array except the one at i.

Example:

>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
>>>foo([3, 2, 1])
[2, 3, 6]
    
from typing import List

def foo(nums: List[int]) -> List[int]:
    product = 1
    for i in nums:
        product*=i
    return [int(product/i) for i in nums]

print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))

--------------------------------------------------------------------------------

Implement a function get_tuple(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.

Example:

>>> get_tuple(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    list=[]
    while(num!=0):
        list.append(num%10)
        num//=10
    list.reverse()
    return tuple(list)

print(get_tuple(87178291199))

--------------------------------------------------------------------------------

Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements. 
The pairs should be formed as in the example. If there is only one element in the list, return [] instead.

Example:

>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
>>> get_pairs([1])
[]

from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    parovi = []
    if len(lst)<=1:
        return []
    for i in range(len(lst)-1):
        parovi.append((lst[i],lst[i+1]))
    return parovi

print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))

--------------------------------------------------------------------------------

Write a Python program to count the frequency of each character in a string (ignore the case of letters).

Example:

Input: 'Oh, it is python'

Output: {" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}

from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    d = {}
    for i in s.lower():
        if i in d and d[i]:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(get_dict('Oh, it is python'))

--------------------------------------------------------------------------------

Write a Python program to print all the unique values of all the dictionaries in a list.

Example:

Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    s = set()
    for i in lst:
        for j in i.values():
            s.add(j)
    return s

print(check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

---

def check2(lst: List[Dict[Any, Any]]) -> Set[Any]:
    return set(j for i in lst for j in i.values())

print(check2([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

--------------------------------------------------------------------------------

Write a program which makes a pretty print of a part of the multiplication table.

Example:

Input:
row_start = 2
row_end = 4
column_start = 3
column_end = 7

Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
that is equal to the following multiplication table:

    3   4   5   6   7   
2   6   8   10  12  14  
3   9   12  15  18  21  
4   12  16  20  24  28

from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    lst=[]
    for i in range(row_start,row_end+1):
        lst_temp=[]
        for j in range(column_start, column_end + 1):
            lst_temp.append(i*j)
        lst.append(lst_temp)
    return lst

row_start = 2
row_end = 4
column_start = 3
column_end = 7
print(check(row_start, row_end, column_start, column_end))

---------------------------------------------------------------------------------

Generate dictionary with squared key value

from typing import Dict

def generate_squares(num: int) -> Dict[int, int]:
    """Generate dictionary with squared key value"""
    d = {}
    for i in range(1, num + 1):
        d[i] = i ** 2
    return d

print(generate_squares(10))
    
--------------------------------------------------------------------------------

Define a function seq_sum(sequence) which allows counting the sum of elements. Elements of all nested sequences should be included.

Example:

def seq_sum(sequence):
    pass
  
sequence = [1,2,3,[4,5, (6,7)]]

>>> print(seq_sum(sequence))
28

from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """ Recursive sum of nested list elements  """
    suma = 0
    for i in sequence:
        if (isinstance(i, int)):
            suma += i
        else:
            suma += seq_sum(i)
    return suma

--------------------------------------------------------------------------------

Define a function linear_seq(sequence) which converts a passed sequence to a sequence without nested sequences.

Example:

def linear_seq(sequence):
    pass
  
sequence = [1,2,3,[4,5, (6,7)]]

>>> print(linear_seq(sequence))
[1,2,3,4,5,6,7]

from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """ Converts a passed sequence to a sequence without nested sequences  """
    lst = []
    for i in sequence:
        if (isinstance(i, int)):
            lst.append(i)
        else:
            for j in linear_seq(i):
                lst.append(j)
    return lst
    
sequence = [1,2,3,[4,5, (6,7)]]
print(linear_seq(sequence))


--------------------------------------------------------------------------------

Create generic union and intersect functions to work with sets. 
The functions must accept an arbitrary number of arguments of different types: list, tuple, and set. 
Each function must return the value of the set type. For example:

>>> union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
{'S', 'P', 'A', 'M', 'C'}

>>> intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
{'S', 'C'}

def union(*args) -> set:
    """ Union of the sets """
    s = set()
    for i in args:
        for j in i:
            s.add(j)
    return s
    #raise NotImplementedError("Implement me!")


def intersect(*args) -> set:
    s = set()
    for i in args[0]:
        ind = True
        for j in args[1:]:
            if(i not in j):
                ind = False
                break
        if ind:
            s.add(i)
    return s
    #raise NotImplementedError("Implement me!")


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))

--------------------------------------------------------------------------------

from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    """Combining dictionaries"""
    d = {}
    for i in args:
        print(i) # ispis argumenta - jednog recnika
        for j in i:
            print(j) # ispis kljuceva tih recnika
            if j in d and d[j]:
                d[j] += i[j] # i[j] - vrednost kljuca
            else:
                d[j] = i[j]
    return d
    pass

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))

print(combine_dicts(dict_1, dict_2, dict_3))

--------------------------------------------------------------------------------

Create a decorator function time_decorator which has to calculate the decorated function execution time 
and put this time value in the execution_time dictionary where the key is the decorated function name. The value is this function's execution time. For example:

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

>>> func_add(10, 20)
30

>>> execution_time['func_add']
0.212341254

from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper_around_original_function(a, b, sl):
        t1 = time.time()
        fn(a, b, sl)
        t2 = time.time()
        global execution_time
        execution_time[f'{fn.__name__}'] = t2 - t1
        return fn(a, b, sl)

    return wrapper_around_original_function

@time_decorator
def func_add(a, b, sl):
    time.sleep(sl)
    return a + b

print(func_add(10, 20, 0.2))

print(execution_time['func_add'])

--------------------------------------------------------------------------------

Write a decorator which logs information about calls of decorated function,
values of its arguments, values of keyword arguments and execution time. Log
should be written to a file.

Example of using

@log
def foo(a, b, c):
    ...

foo(1, 2, c=3)



log.txt

...
foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
...

import time
import inspect


def log(fn):
    def wrapper_around_original_function(*args, **kwargs):
        file1 = open('log.txt', 'w')
        t1 = time.time()
        bound_args = inspect.signature(fn).bind(*args, **kwargs)
        second_dict = bound_args.arguments
        # print(second_dict)
        kwargs_dict = kwargs
        # print(kwargs_dict)
        args_dict = {k: second_dict[k] for k in set(second_dict) - set(kwargs_dict)}
        args_dict = dict(sorted(args_dict.items(), key=lambda x: x[0].lower()))

        fn(*args, **kwargs)

        s = f"{fn.__name__};"
        if (len(args_dict.items()) > 0):
            s += " args: "
            for (k, v) in args_dict.items():
                s += (str(k) + "=" + str(v) + ", ")
            s += ";"
            s = s.replace(", ;", ";")
        if (len(kwargs_dict.items()) > 0):
            s += " kwargs: "
            for (k, v) in kwargs_dict.items():
                s += (str(k) + "=" + str(v) + ", ")
            s += ";"
            s = s.replace(", ;", ";")
        t2 = time.time()
        file1.write(s + f" execution time: {round(t2 - t1, 2)} sec.")
        print(s + f" execution time: {round(t2 - t1, 2)} sec.")
        file1.close()

    return wrapper_around_original_function


@log
def foo(a='default', b='default', c='default', d='default', e='default'):
    print(locals())


@log
def foo1(a='default', b='default', c='default', d='default', e='default'):
    print(locals())


@log
def foo2(a='default', b='default', c='default', d='default', e='default'):
    print(locals())

@log
def foo3(a='default', b='default', c='default', d='default', e='default'):
    print(locals())


foo(1, 2, c=3)

foo1(1, 2, c=3, d=5)

foo2(1, 2, 3)

foo3(c=3, d=5)

--------------------------------------------------------------------------------

Create decorator validate, which validates arguments in the set_pixel function. All function parameters should be between 0(int) and 256(int) inclusive.

If all parameters are valid, the set_pixel function should return a "Pixel created!" message. Otherwise, it should return the "Function call is not valid!" message.

Use functools.wraps where necessary.

Don't forget about doc strings.

def validate(f):
    def wrapper_around_original_function(*args):
        for i in args:
            if i < 0 or i > 256:
                return "Function call is not valid!"
        else:
            return f(*args)
    return wrapper_around_original_function


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"


print(set_pixel(0, 127, 300))
print(set_pixel(0, 127, 250))

--------------------------------------------------------------------------------

Create a decorator factory (decorator itself). 
The factory accepts a function (lambda) as an input and returns a decorator that will return the result of the function as the first argument. 
The result of the decorated function is passed. The function that the factory accepts (in the example below, it is a lambda) can only take one positional parameter.

For example:

>>> @decorator_apply(lambda user_id: user_id + 1)
>>> def return_user_id(num: int): 
        return num
>>> return_user_id(42) 
>>> 43

def decorator_apply(lambda_func):
    def decorator_apply2(f):
        def wrapper_around_original_function(num):
            print("Num: ",num)
            print(f(num))
            print(lambda_func(f(num)))
            print(lambda_func(num))
            return lambda_func(num)
        return wrapper_around_original_function
    return decorator_apply2


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num


print("Konacno: ",return_user_id(100))

---

# dekorator ukrasava funkciju tako sto vraca novu funkciju

# decorator_apply2 ukrasava f (tj. return_user_id)
# decorator_apply ukrasava decorator_apply2 (na izlaz decorator_apply2(f(num) primenjuje lambda_func)

def decorator_apply(lambda_func): # lambda_func = lambda user_id: user_id + 1
    def decorator_apply2(f): # f = return_user_id
        def wrapper_around_original_function(num): # prosledjuje se argument fje return_user_id: num = 100
            print("Num: ",num) # ispisuje se argument koji se prosledjuje dekorisanoj funkciji return_user_id
            print(f(num)) # ispisuje se rezultat return_user_id(num) = 101
            print(lambda_func(f(num))) # f(num) = 101, lambda_func(f(num)) = 102
            print(lambda_func(num)) # lambda_func(num) = 101
            return lambda_func(f(num)) # vraca se vrednost 102
        return wrapper_around_original_function # vraca se ime (kompozicije) funkcije: lambda_func(f)
    return decorator_apply2 # vraca sebe - tj. vraca se lambda_func(f)


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num+1


print(return_user_id(100))
print(return_user_id(150))

--------------------------------------------------------------------------------

Implement a function that works the same as str.split method (without using str.split itself, of course). Pay attention to strings with multiple spaces. For example:

'    Hi     Python    world!' 
Example of the interface:

    def split(data: str, sep=None, maxsplit=-1):
        ...

from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """ Split function   """
    lista = []
    data = data.strip()
    if (data== '' and maxsplit == -1):
        return []
    if (maxsplit == 0):
        return [data]
    if (sep == None):
        sep = ' '
    poz = data.find(sep)
    if (poz >= 0):
        lista.append(f'{data[:poz]}')
        lista.append(split(data[poz + len(sep):], sep, maxsplit - 1))
    else:
        lista.append(f'{data}')
    lista2=[]
    for x in lista:
        if(isinstance(x, list)):
            for i in x:
                lista2.append(i)
        else:
            lista2.append(x)
    return lista2

print(split(' ', sep=','))

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
    
--------------------------------------------------------------------------------

Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by indexes specified in indexes. 
The wrong indexes must be ignored. Examples:

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]

from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    lista: list[str] = []
    j = 0
    for i in indexes:
        if i >= 0:
            lista.append(s[j:i])
            j = i
    if j < len(s):
        lista.append(s[j:])
    return lista


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# ["python", "is", "cool", ",", "isn't", "it?"]

print(split_by_index("no luck", [42]))
# ["no luck"]

--------------------------------------------------------------------------------

Develop a class Field with "full encapsulation" whose attributes are accessed, and data changes are implemented through method calls.

In OOP, it is generally accepted to start the names of the methods for extracting data with the word "get" 
and the names of the methods in which fields are equated to a certain value - "set".

In this task, you must implement get_value and set_value methods for the Field class (__value property).

class Field:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


f = Field(7)
print(f.get_value())
f.set_value(9)
print(f.get_value())

--------------------------------------------------------------------------------

Create a class SchoolMember that represents any person in school. Classes Teacher and Student are inherited from SchoolMember.

Classes should have the same interface as the public show () method. Teacher accepts name (str), age (int), and salary (int). Student accepts name (str), age (int), and grades. Move the same logic of initialization to the class SchoolMember.

Method show() returns a string (see string patterns in the Example).

All attributes that were accepted should be public.

Example
>>> teacher = Teacher("Mr.Snape", 40, 3000)
>>> teacher.name
"Mr.Snape"

>>> persons = [teacher, Student("Harry", 16, 75)]

>>> for person in persons:
       print(person.show())

"Name: Mr.Snape, Age: 40, Salary: 3000"
"Name: Harry, Age: 16, Grades: 75"

class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age)


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Salary: " + str(self.salary)


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Grades: " + str(self.grades)


teacher = Teacher("Mr.Snape", 40, 3000)
print(teacher.name)

persons = [teacher, Student("Harry", 16, 75)]

for person in persons:
    print(person.show())
    
--------------------------------------------------------------------------------

Implement a Counter class that optionally accepts the start value and the counter stop value. If the start value is not specified, the counter should begin with 0. 
If the stop value is not specified, it should be counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."

Implement the two methods: "increment" and "get"

Example:

>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
The maximal value is reached.
>>> c.get()
43

import sys

class Counter:

    def __init__(self, start=0, stop=sys.maxsize):
        self.start = start
        self.stop = stop

    def get(self):
        return self.start

    def increment(self):
        if self.start >= self.stop:
            print("The maximal value is reached.")
            # raise StopIteration
        else:
            self.start += 1
        return self.start


c = Counter(10, 12)
print(c.get())
c.increment()
print(c.get())
c.increment()
print(c.get())
c.increment()
c.increment()
print(c.get())

'''
obj = Counter(27,30) # objekat nema __iter__ metodu i nije iterabilan
for message in obj:  # TypeError: 'Counter' object is not iterable
    obj.increment()
    print(obj.get())
'''

import sys

class Counter:

    def __init__(self, start=0, stop=sys.maxsize):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            print("The maximal value is reached.")
            raise StopIteration
        else:
            self.start += 1
        return self.start


obj = Counter(41, 45)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

numbers = [2, 5, 8]  # iterable
iterator1 = iter(numbers)  # iterator
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

# Ovo izaziva izuzetak StopIteration
'''  
obj = Counter(41, 45)
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
'''

obj = Counter(32)  # Ovo ide dva puta
print(next(iter(obj)))
print(next(iter(obj)))

'''
obj = Counter(41)  # Ovo ide do beskonačnosti
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)
'''

obj = Counter()  # Ovo počinje od 1
print(next(iter(obj)))
print(next(iter(obj)))

obj = Counter()
# for message in obj:  # petlja ide kroz iterabilni objekat
# print(message)

obj = Counter(3, 30)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(start=3, stop=10)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(stop=10)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(10, 12)

--------------------------------------------------------------------------------

Implement a custom dictionary that will memorize the five latest changed keys. Each changed key has to be added in the end of the history data structure.

Using the method "get_history" returns these keys.

Example:

>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()

["bar"]
>>> d.set_value("foo", 44)
>>> d.get_history()
["bar", "foo"]

class HistoryDict:

    def __init__(self, d):
        self.d = d
        self.lst = []

    def set_value(self, key, value):
        self.d[key] = value
        if key in self.lst:
            self.lst.remove(key)
        self.lst.append(key)

    def get_history(self):
        return self.lst if len(self.lst)<5 else self.lst[-5:]


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())

# ["bar"]
d.set_value("foo", 44)
print(d.get_history())
# ["bar", "foo"]

d.set_value("bar", 43)
print(d.get_history())
d.set_value("mar", 43)
print(d.get_history())
d.set_value("gar", 43)
print(d.get_history())
d.set_value("car", 73)
print(d.get_history())
d.set_value("zar", 43)
print(d.get_history())
d.set_value("bar", 56)
print(d.get_history())
d.set_value("zar", 55)
print(d.get_history())
d.set_value("bar", 77)
print(d.get_history())
print(d.d)

--------------------------------------------------------------------------------

You need to create an abstract class Vehicle. Classes Car, Motorcycle, Truck, and Bus are inherited from Vehicle and already implemented.

Class Vehicle accepts the following parameters:

brand_name -> str (e.g. Honda)
year_of_issue -> int (e.g. 2020)
base_price -> int (e.g. 1_000_000)
mileage -> int (e.g. 10_000)
The following methods should be implemented:

vehicle_type - returns str - a type of the vehicle in the following pattern brand_name + name of the class. For example: Toyota Car, Suzuki Motorcycle;
is_motorcycle returning a boolean value depends on the number of wheels (2 wheels -> motorcycle, so the method should return True);
purchase_price - returns the price of the vehicle: (base_price - 0.1 * mileage). If the resulting price is less than 100_000, the method should return 100_000.
Put the following decorators where necessary and if it is necessary:

abstractmethod, classmethod, staticmethod, property, and other decorators.

Example
>>> vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

>>> for vehicle in vehicles:
        print(
            f"Vehicle type={vehicle.vehicle_type()}\n"
            f"Is motorcycle={vehicle.is_motorcycle()}\n"
            f"Purchase price={vehicle.purchase_price}\n"
        )


Vehicle type=Toyota Car
Is motorcycle=False
Purchase price=985000.0

Vehicle type=Suzuki Motorcycle
Is motorcycle=True
Purchase price=796500.0

Vehicle type=Scania Truck
Is motorcycle=False
Purchase price=14915000.0

Vehicle type=MAN Bus
Is motorcycle=False
Purchase price=9905000.0



from abc import ABC
from abc import abstractmethod

class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        return 0

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"

    def is_motorcycle(self) -> bool:
        if(isinstance(self,Motorcycle)):
            return True
        return False

    @property
    def purchase_price(self) -> float:
        return self.base_price - 0.1 * self.mileage


class Car(Vehicle):
    def wheels_num(self):
        return 4


class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


class Truck(Vehicle):
    def wheels_num(self):
        return 10


class Bus(Vehicle):
    def wheels_num(self):
        return 6

vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price}\n"
    )


--------------------------------------------------------------------------------

Implement a pagination class helpful for arranging text on pages and listing content on the given page. 
The class should take in a text and a positive integer, which indicate how many symbols will be allowed per page (take spaces into account as well).

You need to get the number of whole symbols in the text, get the number of pages that came out and the method that accepts the page number, 
and return the number of symbols on this page. If the provided number of the page is missing, raise an exception with the message "Invalid index. Page is missing".

Implement searching/filtering pages by using symbols/words and displaying pages with all the symbols on them. If the provided symbols/words are missing, 
raise an exception with the message "'<symbol/word>' is missing on the pages".

If you're querying by a symbol that appears on many pages or if you are querying by the word that is split in two, return an array of all the occurrences.

Pages indexing starts with 0.

Example:

>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '

import re
class Pagination:
    def __init__(self, data, items_on_page):
        self.__data = data
        self.__items_on_page = items_on_page

    def page_count(self):
        return len(self.__data)//int(self.__items_on_page)+1

    def item_count(self):
        return len(self.__data)

    def count_items_on_page(self, page_number):
        if page_number*self.__items_on_page>self.item_count():
            raise Exception("Invalid index. Page is missing.")
        return self.__items_on_page if page_number < self.page_count()-1 else self.item_count() % self.__items_on_page

    def find_page(self, data):
        pojave = [m.start() for m in re.finditer(data,self.__data)]
        lista = []
        for prvi in pojave:
            for j in range(prvi,prvi+len(data),self.__items_on_page):
                lista.append(j//self.__items_on_page)
        if not lista:
            raise Exception("'"+data+"' is missing on the pages")
        return lista
    
    def display_page(self, page_number):
        return self.__data[page_number*self.__items_on_page:page_number*self.__items_on_page+self.__items_on_page]

pages = Pagination('Your beautiful text', 5)
print(pages.page_count())
#4
print(pages.item_count())
#19

print(pages.count_items_on_page(0))
#5
print(pages.count_items_on_page(3))
#4
#print(pages.count_items_on_page(4))
#Exception: Invalid index. Page is missing.

print(pages.find_page('Your'))
#[0]
print(pages.find_page('e'))
#[1, 3]
print(pages.find_page('beautiful'))
#[1, 2]
#print(pages.find_page('great'))
#Exception: 'great' is missing on the pages

print(pages.display_page(0))


pages = Pagination('Y', 5)
print(pages.item_count())


--------------------------------------------------------------------------------

Write a function divide which accepts a string that contains two integers, separated by spaces (integers can be separated by more than one space). You have to perform the division operation (a / b) and return the result (float) or an error message.

The structure of the error message is the following: Error code: {error message}.

Example
>>> divide("4 2")
2.0

>>> divide("4 0")
"Error code: division by zero"

>>> divide("* 1")
"Error code: invalid literal for int() with base 10: '*'"

'''
def divide(s):
    try:
        if s[2] == "0":
            raise ValueError("That is not a positive number!")
    except ValueError as ve:
        print(ve)
    return int(s[0])/int(s[2])
'''
def divide(s):
    try:
        return int(s[0])/int(s[len(s)-1])
    except Exception as e:
        return "Error code: "+str(e)

#print(divide("2 0"))
#print(divide("2 3"))
print(divide("* 1"))

from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        return int(str_with_ints[0]) / int(str_with_ints[len(str_with_ints) - 1])
    except Exception as e:
        return "Error code: " + str(e)
    #raise NotImplementedError('Implement me!')
    
--------------------------------------------------------------------------------

You have to overload the addition operator in the Counter class. Use the __add__() magic method to overload the addition.

For example, in the case of a + b, the a object should have __add__(), which accepts b as a second parameter (self goes first).

In this case, the Counter object accepts a list from int as a parameter. The object to summarize with will be a str object. The result should be a list of strings with the following pattern: 1 test - one object from list and str separated by the whitespace.

Example
>>> Counter([1, 2, 3]) + "Mississippi"

["1 Mississippi", "2 Mississippi" , "3 Mississippi"]

from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self,other):
        list=[]
        for i in self.values:
            list.append(str(i)+" "+other)
        return list

print(Counter([1,2,3]) + "Misisipi")

--------------------------------------------------------------------------------

Create a hierarchy out of birds. Implement four classes:

Class Bird with an attribute name and methods fly and walk.
Class FlyingBird with attributes name, ration, and with the same methods. ration must have a default value. Implement the method eat, which will describe its typical ration.
Class NonFlyingBird with the same characteristics but obviously without an attribute fly. Add the same "eat" method but with other implementations regarding the swimming bird tastes.
Class SuperBird, which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
Implement a str() function call for each class.

Example:

>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary bird can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats mostly fish"
Look at the mro method or the attribute __mro__ of your last class.


from abc import ABC, abstractmethod
class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        raise AttributeError(self.name + ' object has no attribute fly')
        #raise NotImplementedError("You have to implement fly() method")

    def walk(self):
        print(self.name + " bird can walk")

class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("It eats mostly " + str(self.ration))

    def swim(self):
        print(self.name + " bird can swim")

class FlyingBird(Bird):
    def __init__(self, name, ration=None):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("It eats mostly grains")

    def fly(self):
        print(self.name+" bird can fly")

    def __str__(self):
        return self.name + " bird can walk and fly"

class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name + " bird can walk, swim and fly"

b = Bird("Any")
b.walk()
#"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
p.swim()
#"Penguin bird can swim"
#p.fly()
#AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()
#"It eats mostly fish"

c = FlyingBird("Canary")
print(c)
#"Canary bird can walk and fly"
c.eat()
#"It eats mostly grains"

s = SuperBird("Gull")
print(s)
#"Gull bird can walk, swim and fly"
s.eat()
#"It eats mostly fish"

---

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        raise AttributeError(self.name + ' object has no attribute fly')

    def walk(self):
        return self.name + " bird can walk"

class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return "It eats mostly " + str(self.ration)

    def swim(self):
        return self.name + " bird can swim"

class FlyingBird(Bird):
    def __init__(self, name, ration=None):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return "It eats mostly grains"

    def fly(self):
        return self.name+" bird can fly"

    def __str__(self):
        return self.name + " bird can walk and fly"

class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name + " bird can walk, swim and fly"
        
--------------------------------------------------------------------------------

Implement class Currency and inherited classes Euro, Dollar, and Pound. The course is 1 EUR == 2 USD == 100 GBP

You need to implement the following methods:

course – a classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}

  >>> print(
      f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
      f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
      f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
  )
  Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
  Dollar.course(Pound) ==> 50.0 GBP for 1 USD
  Pound.course(Euro)   ==> 0.01 EUR for 1 GBP
to_currency – this method transforms the currency from one currency to another. The method should return an instance of a required currency.

  >>> e = Euro(100)
  >>> r = Pound(100)
  >>> d = Dollar(200)
  
  >>> print(
      f"e = {e}\n"
      f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
      f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
      f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
  )
  e = 100 EUR
  e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
  e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
  e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed
  
  >>> print(
      f"r = {r}\n"
      f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
      f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
      f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
  )
  r = 100 GBP
  r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
  r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
  r.to_currency(Pound) = 100.0 GBP  # Pound instance printed
+ - returns an instance of a new value

  >>> e = Euro(100)
  >>> r = Pound(100)
  >>> d = Dollar(200)
  >>> print(
      f"e + r  =>  {e + r}\n"
      f"r + d  =>  {r + d}\n"
      f"d + e  =>  {d + e}\n"
  )
  e + r  =>  101.0 EUR  # Euro instance printed
  r + d  =>  10100.0 GBP  # Pound instance printed
  d + e  =>  400.0 USD  # Dollar instance printed
other comparison methods: > < ==

Please pay attention to the examples. Your code should work exactly the same.   


from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:  # argument je tipa klase (Currency)
        return f"{cls.kurs / other_cls.kurs} {other_cls.valuta} for 1 {cls.valuta}"

    def to_currency(self, other_cls: Type[Currency]) -> Type[Currency]:
        return other_cls(self.__class__.kurs / other_cls.kurs * self.value)

    def __add__(self, other) -> Type[Currency]:
        self.value += other.value*(other.__class__.kurs / self.__class__.kurs)
        return self

    def __gt__(self, other):
        return self.value > other.value*(other.__class__.kurs / self.__class__.kurs)

    def __eq__(self, other):
        return self.value == other.value*(other.__class__.kurs / self.__class__.kurs)

    def __lt__(self, other):
        return self.value < other.value*(other.__class__.kurs / self.__class__.kurs)

    def __str__(self):
        return str(self.value) + " " + str(self.__class__.valuta)


class Euro(Currency):
    valuta: str = "EUR"
    kurs: float = 100.0


class Dollar(Currency):
    valuta: str = "USD"
    kurs: float = 50.0


class Pound(Currency):
    valuta: str = "GBP"
    kurs: float = 1.0


print(
    f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
    f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
    f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
)

# Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
# Dollar.course(Pound) ==> 50.0 GBP for 1 USD
# Pound.course(Euro)   ==> 0.01 EUR for 1 GBP

# print(Euro.course(Pound))

e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
    f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
    f"e.to_currency(Euro) = {e.to_currency(Euro)}\n"
)
'''e = 100 EUR
e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
e.to_currency(Euro) = 100.0 EUR  # Euro instance printed'''

print(
    f"r = {r}\n"
    f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
    f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
    f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
)
'''r = 100 GBP
r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
r.to_currency(Euro) = 1.0 EUR  # Euro instance printed
r.to_currency(Pound) = 100.0 GBP  # Pound instance printed'''


print(
      f"e + r  =>  {e + r}\n"
      f"r + d  =>  {r + d}\n"
      f"d + e  =>  {d + e}\n"
  )

'''e + r  =>  101.0 EUR  # Euro instance printed
r + d  =>  10100.0 GBP  # Pound instance printed
d + e  =>  400.0 USD  # Dollar instance printed'''

print(
      f"e > r  =>  {e > r}\n"
      f"r < d  =>  {r < d}\n"
      f"d == e  =>  {d == e}\n"
      f"d > e  =>  {d > e}\n"
  )
    

--------------------------------------------------------------------------------

You must implement the class Book with the attributes price, author, and name.

The author and name fields have to be immutable;
The price field may have changes but has to be in the 0 <= price <= 100 range.
If a user tries to change the author or name fields after an initialization or set price is out of range, the ValueError should be raised.

Implement descriptors PriceControl and NameControl to validate parameters.

Example
>>> b = Book("William Faulkner", "The Sound and the Fury", 12)
>>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
Author='William Faulkner', Name='The Sound and the Fury', Price='12'

>>> b.price = 55
>>> b.price
55
>>> b.price = -12  # => ValueError: Price must be between 0 and 100.
>>> b.price = 101  # => ValueError: Price must be between 0 and 100.

>>> b.author = "new author"  # => ValueError: Author can not be changed.
>>> b.name = "new name"      # => ValueError: Name can not be changed.

class PriceControl:
    """
    Descriptor which don't allow to set price less than 0 and more than 100 included.
    """

    def __set_name__(self, owner, name): # pri postavljanju u konstruktoru self.price = price, uzima iz klase owner (Book) ime za promenljivu name (price)
        self._name = name

    def __set__(self, b, cena):
        if cena < 0 or cena > 100:
            raise ValueError(f'{self._name.capitalize()} must be between 0 and 100.')
        b._price = cena

    def __get__(self, b, objtype=None):
        return b._price

class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __set_name__(self, owner, name): # pri postavljanju u konstruktoru self.name = name, uzima iz klase owner (Book) ime za promenljivu name (name) (slicno i za author)
        self._name = name

    def __set__(self, b, value):
        if self._name in b.__dict__:
            raise ValueError(f'{self._name.capitalize()} can not be changed.')
        b.__dict__[self._name] = value

class Book:

    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author: str = None, name: str = None, price: int = None):
        self.price = price
        self.author = author
        self.name = name


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'

b.price = 55
print(b.price)
# 55

#b.price = -12  # => ValueError: Price must be between 0 and 100.
#b.price = 101  # => ValueError: Price must be between 0 and 100.

#b.author = "new author"  # => ValueError: Author can not be changed.
#b.name = "new name"  # => ValueError: Name can not be changed.

--------------------------------------------------------------------------------

A singleton is a class that only allows a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize a class instance.

Example:

>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True

class Sun:
    instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls.instance is None:
            cls.instance = Sun()
        return cls.instance


p = Sun.inst()
print(id(p))
f = Sun.inst()
print(id(f))
print(p is f)

--------------------------------------------------------------------------------

Implement the keyword encoding and decoding for the Latin alphabet. The keyword cipher uses a keyword to rearrange the letters in the alphabet. 
You should add the provided keyword at the beginning of the alphabet. 
A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. 
The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, 
whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

Encryption:

The keyword is "Crypto"

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Example:

>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"


import string


class Cipher:

    def __init__(self,sifra):
        self.sifra = sifra
        self.alphabet = list(string.ascii_uppercase)
        self.alphabet3 = [j.upper() for j in sifra]
        self.alphabet3.extend([i for i in self.alphabet if i not in self.alphabet3])

    def encode(self, data):
        s = ""
        for i in data:
            s += " " if i == " " else self.alphabet3[self.alphabet.index(i.upper())]
        return s.capitalize()

    def decode(self, data):
        s = ""
        for i in data:
            s += " " if i == " " else self.alphabet[self.alphabet3.index(i.upper())]
        return s.capitalize()


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
#"Btggj vjmgp"

print(cipher.decode("Fjedhc dn atidsn"))
#"Kojima is genius"

--------------------------------------------------------------------------------

Titanic
We want to fill missing values in the 'Age' column  in the 'Titanic'
dataset with median values calculated depending on the prefix in 'Name' column:
For each title from

 ["Mr.", "Mrs.", "Miss."]


We need to use median value calculated for every group.
Find the number of missed values and median values corresponding to every of these 3 groups ('Mr.', 'Mrs.''Miss.'). 
Provide the answer in the form - a list of tuples (Title of the group, number of missed values for the group, median value calculated for the
group). The pattern for the answer is

[('Mr.', x, y), ('Mrs.', k, m), ('Miss.', l, n)]


where x, y, k, m, l, n, are integers, which you should calculate
The median values should be rounded to the nearest integer.

import pandas as pd
import statistics


def get_titatic_dataframe() -> pd.DataFrame:
    df = pd.read_csv("train.csv")
    return df


def get_filled():
    df = get_titatic_dataframe()
    miss = mr = mrs = 0
    age_miss = []
    age_mr = []
    age_mrs = []

    for ind in df.index:
        name = df['Name'][ind]
        age = df['Age'][ind]
        if ("Miss." in name):
            if (str(age) == "nan"):
                miss += 1
            else:
                age_miss.append(int(age))
        if ("Mr." in name):
            if (str(age) == "nan"):
                mr += 1
            else:
                age_mr.append(int(age))
        if ("Mrs." in name):
            if (str(age) == "nan"):
                mrs += 1
            else:
                age_mrs.append(int(age))

    age_mr_med = statistics.median(age_mr)
    age_mrs_med = statistics.median(age_mrs)
    age_miss_med = statistics.median(age_miss)
    return [('Mr.', mr, age_mr_med), ('Mrs.', mrs, age_mrs_med),
                ('Miss.', miss, age_miss_med)]

print(get_filled())

--------------------------------------------------------------------------------

Morze
Write functions code_morse for Morse coding. Notes: The spacebars shoulf be ignored for coding. The Morse letters in coded message should be separated by spacebars
Supplementary: {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 
'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
'1': '.----', '2': '..---', '3': '...--',
'4': '....-', '5': '.....', '6': '-....',
'7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'} 

Example of input: "Data Science - 2023" Example of output: "−·· ·− − ·− ··· −·−· ·· · −· −·−· · −····− ··−−− −−−−− ··−−− ···−−",

st = "Data Science - 2023";
def code_morse(st):
    morse= {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}
    st = st.upper()
    s=""
    for i in st:
        if(i!=' '):
            s+=(morse[i]+" ")
    return s

print(code_morse(st))

--------------------------------------------------------------------------------

Broj kompozicija i particija
na primer za n=4:
particije: 4, 3+1, 2+2, 2+1+1, 1+1+1+1
kompozicije: 4, 3+1, 1+3, 2+2, 2+1+1, 1+2+1, 1+1+2, 1+1+1+1

n=5

def kompozicije(k):
    if(k==0):
        return 1
    suma = 0
    for i in range(k,0,-1):
        suma += kompozicije(k-i)
    return suma
    
def particije(k,j):
    if(k==0):
        return 1
    suma = 0
    for i in range(min(k,j),0,-1):
        suma += particije(k-i,i)
    return suma

print("#:",kompozicije(n))
print("--------")
print("#:",particije(n, n))

Ispis kompozicija i particija

n=5

def kompozicije(k,s):
    if(k==0):
        print(s)
        return

    for i in range(k,0,-1):
        kompozicije(k-i,s+str(i))

def particije(k,j,s):
    if(k==0):
        print(s)
        return

    for i in range(min(k,j),0,-1):
        particije(k-i,i,s+str(i))

kompozicije(n, "")
print("--------")
particije(n, n, "")

Ispis i broj kompozicija i particija

n=5

def kompozicije(k,s):
    if(k==0):
        print(s)
        return 1
    suma = 0
    for i in range(k,0,-1):
        suma += kompozicije(k-i,s+str(i))
    return suma
    
def particije(k,j,s):
    if(k==0):
        print(s)
        return 1
    suma = 0
    for i in range(min(k,j),0,-1):
        suma += particije(k-i,i,s+str(i))
    return suma

print("#:",kompozicije(n, ""))
print("--------")
print("#:",particije(n, n, ""))

-------------------------------------------------------------------------------

# Kompozicije
n = 5
lista = [0]*n
def komp(n,lista,j):
    if(n==0):
        print(lista)
    for i in range(n,0,-1):
        lista[j] = i
        komp(n-i,lista.copy(),j+1)
    
komp(n,lista,0)
print("----------------")

# Kompozicije bez nula clanova
n = 5
lista = [0]*n
def komp(n,lista,j):
    if(n==0):
        print([x for x in lista if x is not 0])
    for i in range(n,0,-1):
        lista[j] = i
        komp(n-i,lista.copy(),j+1)
    
komp(n,lista,0)

print("----------------")

n = 5
def kompoz2(n, a):
    if n == 0:
        print(a)
        return
    for i in range(n, 0, -1):
        kompoz2(n - i, a + str(i))

print("----------------")

kompoz2(n, "")

def kompoz3(n, a, sve):
    if n == 0:
        sve.append(a)
        print(a)
        return
    for i in range(n, 0, -1):
        kompoz3(n - i, a + str(i), sve)
    return sve

n = 5
print(kompoz3(n, "", []))

print("----------------")

Ispisati kompozicije kao stringove

n = 5

def komp(n, a, j):
    if (n == 0):
        print(a)
    for i in range(n, 0, -1):
        a += str(i)
        komp(n - i, a, j + 1)
        a = a[:-1]


komp(n, "", 0)

def komp2(n, a, j):
    if (n == 0):
        print(a)
    for i in range(n, 0, -1):
        komp2(n - i, a + str(i), j + 1)


komp2(n, "", 0)

print("----------------")

Prebrojati kompozicije:

def kompoz5(n):
    if n == 1:
        return 1
    s = 1
    for i in range(n - 1, 0, -1):
        s += kompoz5(i)
    return s

n = 30   
print(kompoz5(n))    
    
print("----------------")

Prebrojati kompozicije (uz pamcenje (dinamicko programiranje)):

mem = [0]*(n+1)
def kompoz6(n):
    if mem[n] != 0:
        return mem[n]
    if n == 1:
        return 1
    s = 1
    for i in range(n - 1, 0, -1):
        s += kompoz6(i)
    mem[n] = s
    return s

n = 900 
print(kompoz6(n))

Generalno: komp(n) = 2**(n-1)

--------------------------------------------------------------------------------

#Particije
n = 5
lista = [0]*n
def part(n,k,lista,j):
    if(n==0):
        print(lista)
        return
    for i in range(n,0,-1):
        if i >= k:
            lista[j] = i
            part(n-i,i,lista.copy(),j+1)
    
part(n,0,lista,0)  # u pozivu je drugi argument 0

print("----------------")

#Particije bez nula clanova
n = 5
lista = [0]*n
def part(n,k,lista,j):
    if(n==0):
        print([x for x in lista if x is not 0])
        return
    for i in range(n,0,-1):
        if i >= k:
            lista[j] = i
            part(n-i,i,lista.copy(),j+1)
    
part(n,0,lista,0)  # u pozivu je drugi argument 0

print("----------------")

#Particije 
n = 5
lista = [0]*n
def part(n,k,lista,j):
    if(n==0):
        print(lista)
        return
    for i in range(min(n,k),0,-1):
        lista[j] = i
        part(n-i,i,lista.copy(),j+1)
    
part(n,n,lista,0)  # u pozivu je drugi argument n

print("----------------")

#Particije bez nula clanova
n = 5
lista = [0]*n
def part(n,k,lista,j):
    if(n==0):
        print([x for x in lista if x is not 0])
        return
    for i in range(min(n,k),0,-1):
        lista[j] = i
        part(n-i,i,lista.copy(),j+1)
    
part(n,n,lista,0) # u pozivu je drugi argument n

print("----------------")

n = 60

Prebrojati particije:

def part(n, k):
    if n == 0:
        return 1
    s = 0
    for i in range(n, 0, -1):
        if i >= k:
            s += part(n - i, i)
    return s


print(part(n, 0))

print("----------------")

def part2(n, k):
    if n == 0:
        return 1
    s = 0
    for i in range(min(n, k), 0, -1):
        s += part2(n - i, i)
    return s
    
    
print(part2(n, n))

print("----------------")

Prebrojavanje particija bez pamcenja:

# part(n, k) = part(n, k - 1) + part(n - k, k) 
# npr. part(5,3) = part(5,2) + part(2,3)
# part(5,3) = {5,4+1,3+2,3+1+1,2+2+1} 
# part(5,2) = {5,4+1,3+2}
# part(2,3) = {2,1+1} = kada se svakom sabirku iz {3+1+1,2+2+1} oduzme 1.

def part3(n, k):
    if n < 0:
        return 0
    if n <= 1 or k <= 1:
        return 1
    return part3(n, k - 1) + part3(n - k, k) 

print(part3(n, n))

Prebrojavanje particija sa pamcenjem:

n = k = 600
mem = [[0 for j in range(k+1)] for i in range(n+1)]
    
def part4(n, k):
    if n < 0:
        return 0
    if n <= 1 or k <= 1:
        return 1
    if mem[n][k] != 0:
        return mem[n][k]
    mem[n][k] = part4(n, k - 1) + part4(n - k, k)
    return mem[n][k]
    
print(part4(n,n))

--------------------------------------------------------------------------------

Ispisati sve permutacije zadate liste

a = [1,2,3,4]
def perm(a,s):
    if(len(a)==0):
        print(s)
        return
    for i in range(len(a)):
        s.append(a[i])
        perm(a[:i]+a[i+1:],s.copy())
        s = s[:-1]
        
perm(a,[])

print("--------------")

a = [1,2,3,4]
def perm2(a,s):
    if(len(a)==0):
        print(s)
        return
    for i in range(len(a)):
        s+=str(a[i])
        perm2(a[:i]+a[i+1:],s)
        s = s[:-1]
      
perm2(a,"")

print("--------------")
        
a = "1234"
def perm3(a,s):
    if(len(a)==0):
        print(s)
        return
    for i in range(len(a)):
        s+=str(a[i])
        perm3(a.replace(a[i],""),s)
        s = s[:-1]
        
perm3(a,"")

print("--------------")
        
a = "1234"
def perm4(a,s):
    if(len(a)==0):
        print(s)
        return
    for i in range(len(a)):
        perm4(a.replace(a[i],""),s+str(a[i]))
        
perm4(a,"")

print("--------------")
        
a = "1234"
def perm5(a,s):
    if(len(a)==0):
        print(s)
    else:
        for i in range(len(a)):
            perm5(a.replace(a[i],""),s+str(a[i]))
        
perm5(a,"")

print("--------------")


a = [0,1,2,3]
def perm2(a,s):
    if(len(a)==0):
        print(s)
        return # OVDE RETURN MOZE DA SE IZOSTAVI POSTO SE ULAZNI NIZ SMANJUJE (OVDE JE PRAZAN)
    for j in range(len(a)): 
        b = [x for i,x in enumerate(a) if i!=j] 
        s_pom = s.copy()
        s_pom.append(a[j])
        perm2(b,s_pom)
        
perm2(a,[])

---------------------------------------------------------

Sprat zgrade (od n spratova) može biti obojen u jednu od boja (plava, crvena, bela)

# Ispis broja mogucnosti za tri boje i n spratova
n = 3
broj = 0


def fun(boja, n):
    global broj
    if (n == 0):
        broj += 1
        return
    fun("P", n - 1)
    fun("C", n - 1)
    fun("B", n - 1)


fun("", n)
print(broj)

# Ispis broja mogucnosti za tri boje i n spratova (skracen zapis)
broj = 0


def fun2(boja, n):
    global broj
    if (n == 0):
        broj += 1
        return
    for i in ["P", "C", "B"]:
        fun2(i, n - 1)


fun2("", n)
print(broj)

# Ispis broja mogucnosti bez onih kada su dve iste boje jedna pored druge
broj = 0


def fun3(boja, n):
    global broj
    if (n == 0):
        broj += 1
        return
    for i in ["P", "C", "B"]:
        if (boja != i):
            fun3(i, n - 1)


fun3("", n)
print(broj)

# Ispis broja mogucnosti bez onih kada su dve crvene boje jedna pored druge
broj = 0


def fun4(boja, n):
    global broj
    if (n == 0):
        broj += 1
        return
    for i in ["P", "C", "B"]:
        if (boja == i and boja == "C"):
            continue
        fun4(i, n - 1)


fun4("", n)
print(broj)

# Ispis broja mogucnosti bez onih kada su tri boje jedna pored druge
broj = 0


def fun5(boja, n, ind):
    global broj
    if (n == 0):
        broj += 1
        return
    for i in ["P", "C", "B"]:
        if (ind == True and boja == i):
            continue
        if (boja == i):
            fun5(i, n - 1, True)
        else:
            fun5(i, n - 1, False)


fun5("", n, False)
print(broj)

# Ispis broja mogucnosti bez onih kada su tri crvene boje jedna pored druge
broj = 0


def fun6(boja, n, ind):
    global broj
    if (n == 0):
        broj += 1
        return
    for i in ["P", "C", "B"]:
        if (ind == True and i == "C"):
            continue
        if (boja == i and boja == "C"):
            fun6(i, n - 1, True)
        else:
            fun6(i, n - 1, False)


fun6("", n, False)
print(broj)

print("------------------")
# Ispis broja mogucnosti za tri boje i n spratova bez globalne promenljive za sumu
n = 3


def fun7(boja, n):
    if (n == 0):
        return 1
    broj = 0
    broj += fun7("P", n - 1)
    broj += fun7("C", n - 1)
    broj += fun7("B", n - 1)
    return broj


print(fun7("", n))

# Skraceni ispis broja mogucnosti za tri boje i n spratova bez globalne promenljive za sumu
n = 3


def fun8(boja, n):
    if (n == 0):
        return 1
    broj = 0
    for i in ["P", "C", "B"]:
        broj += fun8(i, n - 1)
    return broj


print(fun8("", n))

# Ispis svih mogucnosti i broja mogucnosti za tri boje i n spratova bez globalne promenljive za sumu
n = 3


def fun9(boja, n, s):
    if (n == 0):
        print(s)
        return 1
    broj = 0
    for i in ["P", "C", "B"]:
        broj += fun9(i, n - 1, s + i)
    return broj


print(fun9("", n, ""))


# Ispis svih mogucnosti bez onih kada su dve iste boje jedna pored druge
def fun10(boja, n, s):
    if (n == 0):
        print(s)
        return
    for i in ["P", "C", "B"]:
        if (boja != i):
            fun10(i, n - 1, s + i)


fun10("", n, "")

print("---------------")


# Ispis svih mogucnosti bez onih kada su dve crvene boje jedna pored druge
def fun11(boja, n, s):
    if (n == 0):
        print(s)
        return
    for i in ["P", "C", "B"]:
        if (boja != i or boja != "C"):
            fun11(i, n - 1, s + i)


fun11("", n, "")

print("---------------")


# Ispis svih mogucnosti bez onih kada su tri boje jedna pored druge
def fun12(boja, n, s, ind):
    if (n == 0):
        print(s)
        return
    for i in ["P", "C", "B"]:
        if (ind != True or boja != i):
            if (boja == i):
                fun12(i, n - 1, s + i, True)
            else:
                fun12(i, n - 1, s + i, False)


fun12("", n, "", False)

print("---------------")


# Ispis svih mogucnosti bez onih kada su tri crvene boje jedna pored druge
def fun13(boja, n, s, ind):
    if (n == 0):
        print(s)
        return
    for i in ["P", "C", "B"]:
        if (ind != True or boja != i):
            if (boja == i and boja == "C"):
                fun13(i, n - 1, s + i, True)
            else:
                fun13(i, n - 1, s + i, False)


fun13("", n, "", False)

print("---------------")


# Ispis svih mogucnosti i broja mogucnosti bez onih kada su tri crvene boje jedna pored druge
def fun14(boja, n, s, ind):
    if (n == 0):
        print(s)
        return 1
    broj = 0
    for i in ["P", "C", "B"]:
        if (ind != True or boja != i):  # uslov nece proci samo kada su prethodne dve boje C i boje=i (znaci i ona je C)
            if (boja == i and boja == "C"):
                broj += fun14(i, n - 1, s + i, True)
            else:
                broj += fun14(i, n - 1, s + i, False)
    return broj


print(fun14("", n, "", False))

----------DRUGI POGLED NA PROBLEM BOJENJA ZGRADE-------------------

Broj mogućih spratova zgrade (od mogućih boja: plava, crvena i bela) bez dva uzastopna crvena sprata:

"""
Sprat zgrade od n spratova boji se sa tri boje (plava, crvena, bela).
Na koliko načina se zgrada može obojiti ako ne mogu dva crvena sprata da budu uzastopna.
"""
Kada tražimo f(n), pretpostavimo da znamo f(k) za k<n (tj. da je problem rešen za k<n).

- crveni sprat nije poslednji: onda on mora biti plav ili beo, dakle 2*f(n-1) mogućnosti
- crveni sprat jeste poslednji: pre nje mora biti plava ili crvena, dakle 2*f(n-2) mogućnosti 

n = 35

def fun4(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return 2*fun4(n-1) + 2*fun4(n-2)

print(fun4(n))

print("------5--------")

mem = [0]*(n+1)
def fun5(n):
    if mem[n] != 0:
        return mem[n]
    if n == 0:
        mem[n] = 1
        return 1
    if n == 1:
        mem[n] = 3
        return 3
    mem[n] = 2*fun5(n-1) + 2*fun5(n-2)
    return mem[n]

print(fun5(n))
print(mem)

print("------6--------")

def fun6(n):
    a = 3
    b = 1
    for i in range (2,n+1):
        c = 2*(a + b)
        b = a
        a = c
    return c

print(fun6(n))

---------------------------------------

Broj i ispis zgrada bez tri uzastpna sprata crvene boje:

n  = 7

def fun14(boja, n, s, ind):
    if (n == 0):
        print(s)
        return 1
    broj = 0
    for i in ["P", "C", "B"]:
        if (ind != True or boja != i):  # uslov nece proci samo kada su prethodne dve boje C i boje=i (znaci i ona je C)
            if (boja == i and boja == "C"):
                broj += fun14(i, n - 1, s + i, True)
            else:
                broj += fun14(i, n - 1, s + i, False)
    return broj


print(fun14("", n, "", False))

Broj zgrada bez tri uzastpna sprata crvene boje posmatranjem već rešenih potproblema

def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 9
    return 2*f(n-1)+2*f(n-2)+2*f(n-3) # repna rekurzija

print(f(n))

Rekurzivno rešenje uz pamćenje već izračunatih vrednosti (dinamičko programiranje)

mem = [0]*(n+1)
def f2(n):
    if mem[n]!=0:
        return mem[n]
    if n == 0:
        mem[n] = 1
        return 1
    if n == 1:
        mem[n] = 3
        return 3
    if n == 2:
        mem[n] = 9
        return 9
    mem[n] = 2*f2(n-1)+2*f2(n-2)+2*f2(n-3)
    return mem[n]

print(f2(n))
print(mem)

Iterativno rešenje:

def f3(n):
    a = 9
    b = 3
    c = 1
    for i in range(3,n+1):
        d = 2*(a+b+c)
        c = b
        b = a
        a = d
    return d

print(f3(n))

Generalno, neka se spratovi n-tospratnice boje jednom od mogućih boja P, C ili B.
Broj mogućih bojenja zgrade bez x uzastopnih spratova iste zadate boje je:

f(n) = 2*(f(n-1)+f(n-2)+f(n-3)+...+f(n-x)) uz početne uslove f(i)=x**i (i=0,...,x-1)

--------------------FIBONAČIJEV NIZ--------------------------

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

n = 40
print(fib(n,[0]*(n+1)))

def fib_mem(n,mem):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mem[n]!=0:
        return mem[n]
    mem[n] = fib_mem(n-1,mem)+fib_mem(n-2,mem)
    return mem[n] 

def iter_fib(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c
    
n = 900
print(iter_fib(n))
print(fib_mem(n,[0]*(n+1)))

--------------------PROBLEM POPUNJAVANJA RANCA--------------------------

Računanje maksimalne dozovoljene popunjenosti preko globalne promenljive

import random as rd

n = 10
a = [0]*n
t = []
kap = 40
max = 0
t = [kap*rd.random() for i in range(n)]
print(t)

def fun(n,a,i,tez):
    global max
    if(i==n):
        if tez > max and tez <= kap:
            max = tez
            #print(a)
        return
    a[i] = 0
    fun(n,a,i+1,tez+a[i]*t[i])
    a[i] = 1
    fun(n,a,i+1,tez+a[i]*t[i])
    
fun(n,a,0,0)
print("Max popunjenost: ",max)

---

Odsecanje nepotrebnih grana:

import random as rd

n = 10
a = [0]*n
kap = 40
t = [kap*rd.random() for i in range(n)]
print(t)

def fun(a,i,tez):
    if(i==n):
        print(a,tez)
        return 
    a[i] = 0
    if tez+a[i]*t[i] <= kap:
        fun(a,i+1,tez+a[i]*t[i])
    a[i] = 1
    if tez+a[i]*t[i] <= kap:
        fun(a,i+1,tez+a[i]*t[i])
        
fun(a,0,0)

---

Računanje maksimalne dozvoljene popunjenosti

import random as rd

n = 10
a = [0]*n
kap = 40
t = [kap*rd.random() for i in range(n)]
print(t)

def fun(a,i,tez):
    if(i==n):
        print(a,tez)
        return 0
    maxi = 0
    a[i] = 0
    if tez+a[i]*t[i] <= kap:
        s =  a[i]*t[i]+fun(a,i+1,tez+a[i]*t[i])
        if s>maxi:
            maxi = s
    a[i] = 1
    if tez+a[i]*t[i] <= kap:
        s =  a[i]*t[i]+fun(a,i+1,tez+a[i]*t[i])
        if s>maxi:
            maxi = s
    return maxi
        
print("\nMaksimalna popunjenost je ",fun(a,0,0))

---

Skraćeni zapis prethodnog

import random as rd

n = 10
a = [0]*n
kap = 40
t = [kap*rd.random() for i in range(n)]
print(t)

def fun(a,i,tez):
    if(i==n):
        print(a,tez)
        return 0
    maxi = 0
    for k in range(2):
        a[i] = k
        if tez+a[i]*t[i] <= kap:
            s =  a[i]*t[i]+fun(a,i+1,tez+a[i]*t[i])
            if s>maxi:
                maxi = s
    return maxi
        
print("\nMaksimalna popunjenost je ",fun(a,0,0))

---

Dodatni ispis stavki koje učestvuju u maksimalnoj mogućoj popunjenosti

import random as rd

def fun(a,i,tez):
    if(i==n):
        # print(a,tez)  # ispis dozvoljenih kombinacija
        d[tuple(a)] = round(tez,3)
        return 0
    maxi = 0
    for k in range(2):
        a[i] = k
        if tez+a[i]*t[i] <= kap:
            s =  a[i]*t[i]+fun(a,i+1,tez+a[i]*t[i])
            if s>maxi:
                maxi = s
    return maxi

n = 30
a = [0]*n
kap = 400
t = [kap*rd.random() for i in range(n)]
print("Slucajne tezine predmeta :\n",t)
d = {}

max_pop = fun(a,0,0)       
print("\nMaksimalna popunjenost je ",max_pop)
print("Izabrane stavke: ",list(d.keys())[list(d.values()).index(round(max_pop,3))]) 

---OPTIMALNO REŠENJE---

# stavke = [12,6,3,7]
stavke = [12, 6, 7]
kap = 15  # 20

def popuni(n, kap):
    if n == 0:
        return 0
    a = popuni(n - 1, kap)  # popuni(2,15) treba da vrati 12 
    b = 0
    if kap - stavke[n - 1] >= 0:
        b = stavke[n - 1] + popuni(n - 1, kap - stavke[n - 1])  # ovo treba da vrati 7 + popuni(2,8)
    return max(a, b)


print(popuni(1, kap))
print("-------------------")
print(popuni(2, kap))
print("-------------------")
print(popuni(3, kap))

---

import random,time

n = 110
kap = 1100000
stavke = [random.randint(1,kap) for i in range(n)]
print(stavke)

def popuni5(n, kap):
    if n == 0:
        return 0
    if kap - stavke[n - 1] >= 0:
        return max(popuni5(n - 1, kap), stavke[n - 1] + popuni5(n - 1, kap - stavke[n - 1]))
    return popuni5(n - 1, kap)

startTime = time.time()
print(popuni5(n, kap))
stopTime = time.time()
print('Time:', (stopTime - startTime))

---

mem = [[0 for j in range(kap+1)] for i in range(n+1)]

def popuni2(n, kap):
    if n == 0:
        return 0
    if mem[n-1][kap] == 0:
        mem[n-1][kap] = popuni2(n - 1, kap)
    a = mem[n-1][kap]
    b = 0
    if kap - stavke[n - 1] >= 0:
        if mem[n-1][kap - stavke[n - 1]] == 0:
            mem[n-1][kap - stavke[n - 1]] = popuni2(n - 1, kap - stavke[n - 1]) 
        b = stavke[n - 1] + mem[n-1][kap - stavke[n - 1]]  
    return max(a, b)

startTime = time.time()
print(popuni2(n, kap))
stopTime = time.time()
print('Time:', (stopTime - startTime))

---

mem = [[0 for j in range(kap+1)] for i in range(n+1)]
def popuni4(n, kap):
    if n == 0:
        return 0
    if mem[n-1][kap] == 0:
        mem[n-1][kap] = popuni4(n - 1, kap)
    b = 0
    if kap - stavke[n - 1] >= 0:
        if mem[n-1][kap - stavke[n - 1]] == 0:
            mem[n-1][kap - stavke[n - 1]] = popuni4(n - 1, kap - stavke[n - 1]) 
        b = stavke[n - 1] + mem[n-1][kap - stavke[n - 1]] 
    return max(mem[n-1][kap], b)
    
---

mem = [[0 for j in range(kap+1)] for i in range(n+1)]
def popuni3(n, kap):
    if n == 0:
        return 0
    if mem[n-1][kap] == 0:
        mem[n-1][kap] = popuni3(n - 1, kap)
    if kap - stavke[n - 1] >= 0:
        if mem[n-1][kap - stavke[n - 1]] == 0:
            mem[n-1][kap - stavke[n - 1]] = popuni3(n - 1, kap - stavke[n - 1]) 
        return max(mem[n-1][kap], stavke[n - 1] + mem[n-1][kap - stavke[n - 1]])
    return mem[n-1][kap]

startTime = time.time()
print(popuni3(n, kap))
stopTime = time.time()
print('Time:', (stopTime - startTime))

---------------------------------------------

Za dati ti ceo broj (kap) pronaći najmanji mogući broj novčića za njegovo rastavljanje:


novcici = [1,6,10]
#kap = 13    # 3: 1+6+6
#kap = 49    # 7: 1+6+6+6+10+10+10
kap = 55     # 8: 1+6+6+6+6+10+10+10

def rastavi0(n,br):
    if n==0:
        return br
    mini = kap + 1
    for i in novcici:
        if n-i>=0:  
            pom = rastavi0(n-i,br+1)
        if mini>pom:
            mini = pom
    return mini
            
print(rastavi0(kap,0))

---

def rastavi3(n):
    if n==0:
        return 0
    mini = kap + 1
    for i in novcici:
        if n-i>=0:  
            pom = 1 + rastavi3(n-i)
        if mini>pom:
            mini = pom
    return mini
            
print(rastavi3(kap))

---

def rastavi4(n,br,s):
    if n==0:
        return br,s
    mini = kap + 1
    ss = ""
    for i in novcici:
        if n-i>=0:  
            pom,st = rastavi4(n-i,br+1,s+"|"+str(i))
        if mini>pom:
            mini = pom
            ss = st
    return mini,ss
            
print(rastavi4(kap,0,""))

-------------------------------------------------------------------------------------

Problem Hanojskih kula: n diskova sa stuba source prebaciti na stub destination preko pomoćnog diska auxiliary.
Veći disk ne sme da se nalazi na manjem. 
Rekurzivna ideja:
1. Prebaciti manjih n-1 diskova sa source na auxiliary preko destination
2. Preostali najveći disk prebaciti sa source na destination
3. Prebaciti manjih n-1 diskova sa auxiliary na destination preko source

# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
    if n== 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods

-------------------------------------------------------------------------------------

Implementirati binarnu pretragu (sortiranog niza)

# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


----------------------------POVEZANE LISTE----------------------------------------------------

Demonstrirati osnovne operacije sa povezanom listom.

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # ispis liste
    def pisi(self):
        pom = self.head
        while pom != None:
            print(pom.data, end=" ")
            pom = pom.next

    # provera da li element x postoji u listi
    def pronadji(self, x):
        pom = self.head
        while pom != None:
            if pom.data == x:
                return True
            pom = pom.next
        return False

    # duzina liste
    def len(self):
        brojac = 0
        pom = self.head
        while pom != None:
            brojac += 1
            pom = pom.next
        return brojac

    # pronalaženje elementa liste na poziciji index
    def pronadji_po_indeksu(self, index):
        pom = self.head
        if (self.len() <= index):
            return -1
        if index == 0:
            return pom.data
        for _ in range(index):
            pom = pom.next
        return pom.data

    # dodavanje novog elementa na kraj liste
    def dodaj_na_kraj(self, x):
        pom = self.head
        while pom.next != None:
            pom = pom.next
        pom.next = Node(x)

    # rekurzivni ispis liste
    def pisi_rek(self,head):
        if head == None:
            return
        print(head.data, end=" ")
        self.pisi_rek(head.next)

    # rekurzivni ispis liste u inverznom poretku
    def pisi_rek_inverzno(self, head):
        if head == None:
            return
        self.pisi_rek_inverzno(head.next)
        print(head.data, end=" ")
        
    # okretanje veza u matičnoj listi - pravljenje reverzne liste
    def reverseLinkedList2(self):
        previous = None
        current = self.head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    # okretanje veza u zadatoj listi - pravljenje reverzne liste
    def reverseLinkedList(self, myLinkedList):
        previous = None
        current = myLinkedList.head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        myLinkedList.head = previous


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)
    llist.pisi()
    print()
    print(llist.pronadji_po_indeksu(5))
    print(llist.pronadji(30))
    llist.dodaj_na_kraj(77)
    llist.pisi()
    print()
    llist.pisi_rek(llist.head)
    print()
    llist.pisi_rek_inverzno(llist.head)
    llist.reverseLinkedList(llist)
    print()
    llist.pisi()
    llist.reverseLinkedList2()
    print()
    llist.pisi()

--------------------------------------------------------------------------------

Demonstrirati osnovne operacije sa povezanom listom.

# Create a Node class to create a node

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create a LinkedList class

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to add a node at begin of LL
	def insertAtBegin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

	# Method to add a node at any index
	# Indexing starts from 0.
	def insertAtIndex(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insertAtBegin(data)
		else:
			while current_node != None and position+1 != index:
				position = position+1
				current_node = current_node.next

			if current_node != None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

	# Method to add a node at the end of LL

	def insertAtEnd(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		current_node = self.head
		while current_node.next:
			current_node = current_node.next

		current_node.next = new_node

	# Update node of a linked list
	# at given position
	def updateNode(self, val, index):
		current_node = self.head
		position = 0
		if position == index:
			current_node.data = val
		else:
			while current_node != None and position != index:
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.data = val
			else:
				print("Index not present")

	# Method to remove first node of linked list

	def remove_first_node(self):
		if self.head == None:
			return

		self.head = self.head.next

	# Method to remove last node of linked list
	def remove_last_node(self):

		if self.head is None:
			return

		current_node = self.head
		while current_node.next.next:
			current_node = current_node.next

		current_node.next = None

	# Method to remove at given index
	def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while current_node != None and position+1 != index:
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

	# Method to remove a node from linked list
	def remove_node(self, data):
		current_node = self.head

		if current_node.data == data:
			self.remove_first_node()
			return

		while current_node != None and current_node.next.data != data:
			current_node = current_node.next

		if current_node == None:
			return
		else:
			current_node.next = current_node.next.next

	# Print the size of linked list
	def sizeOfLL(self):
		size = 0
		if self.head:
			current_node = self.head
			while current_node:
				size = size+1
				current_node = current_node.next
			return size
		else:
			return 0

	# print method for the linked list
	def printLL(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)


# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())

------------------------------------------------------

Rekurzivni rad sa listom

# Recursive Python program to
# search an element in linked list
 
# Node class
class Node:
     
    # Function to initialise
    # the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
 
class LinkedList:
     
    def __init__(self):
        self.head = None # Initialize head as None
 
    # This function insert a new node at
    # the beginning of the linked list
    def push(self, new_data):
     
        # Create a new Node
        new_node = Node(new_data)
 
        # Make next of new Node as head
        new_node.next = self.head
 
        # Move the head to
        # point to new Node
        self.head = new_node
     
     
    # Checks whether the value key
    # is present in linked list
    def search(self, li, key):
         
        # Base case
        if(not li):
            return False
         
        # If key is present in
        # current node, return true
        if(li.data == key):
            return True
         
        # Recur for remaining list
        return self.search(li.next, key)
    
    
    # This function counts number of nodes in Linked List
    # recursively, given 'node' as starting node.
    def getCountRec(self, node):
        if (not node): # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)
  
    # A wrapper over getCountRec()
    def getCount(self):
       return self.getCountRec(self.head)
    
    def traverse(self,head):
        if (head == None):
            return
     
        # If head is not None, print current node
        # and recur for remaining list
        print(head.data, end = " ");
        self.traverse(head.next)
        
    def traverseMain(self):
        self.traverse(self.head)
        
    # Function to Check Linked List is
    # sorted in descending order or not
    def isSortedDesc(self,head):    
        # Base cases
        if (head == None or head.next == None):
            return True
      
        # Check first two nodes and recursively
        # check remaining.  
        return (head.data > head.next.data and
           isSortedDesc(head.next))
        
    def isSortedDescMain(self):
        self.isSortedDesc(self.head)
    
# Driver Code           
if __name__=='__main__':
 
    li = LinkedList()
     
    li.push(1)
    li.push(2)
    li.push(3)
    li.push(4)
     
    key = 4
     
    if li.search(li.head,key):
        print("Yes")
    else:
        print("No")
        
    li.traverseMain()
    print ("Count of nodes is :",li.getCount())
    
    if (llist.isSortedDescMain()):
        print("Yes");
    else:
        print("No");

--------------------------STABLA------------------------------------------------------

# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val,end=" ")
 
        # now recur on right child
        printInorder(root.right)
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val,end=" ")
 
 
# A function to do preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val,end=" ")
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
 
print("\nInorder traversal of binary tree is")
printInorder(root)
 
print("\nPostorder traversal of binary tree is")
printPostorder(root)

--------------------------------------------------------------------------------

Visina stabla je broj grana koje povezuju koren stabla i najudaljeniji list.
Pronaći visinu stabla pretragom u širinu.

# Python3 program to find the height of a tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


# Function to find height of tree
def height(root):
    # Base Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    q = []

    # Enqueue Root and initialize height
    q.append(root)
    height = 0

    # Loop while queue is not empty
    while q:

        # nodeCount (queue size) indicates number of nodes
        # at current level
        nodeCount = len(q)

        # Dequeue all nodes of current level and Enqueue all
        # nodes of next level
        while nodeCount > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            nodeCount -= 1
        if q:
            height += 1

    return height


# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

print("Height(Depth) of tree is", height(root))

--------------------------------------------------------------------------------

Pronaći visinu stabla pretragom u dubinu (verzija 1).
Problem se svodi na maksimum visine levog i desnog podstabla.
    
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def tree_height(self, root):
        if root is None:
            return 0
        return max(1 + self.tree_height(root.left), 1 + self.tree_height(root.right))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    print(root.tree_height(root))
    
---

Pronaći visinu stabla pretragom u dubinu (verzija 2).

# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)

print("Height of tree is %d" % (maxDepth(root)))

--------------------------------------------------------------------------------

Prebrojati listove u stablu (problem se svodi na sumu listova u levom i desnom podstablu)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def countLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('Count of leaf nodes:', countLeafNodes(root))

----------------------------GRAFOVI----------------------------------------------------

Graf je struktura sastavljena od objekata (čvorova) koji su povezani vezama (granama).
Na primer, čvorovi su gradovi, a grane putevi između njih. Ako su putevi jednosmerni,
graf je usmeren; u suprotnom je neusmeren. Teorijski, gradovi (čvorovi) mogu biti izolovani.

Implementirati graf preko matrice povezanosti koja je predstavljena preko rečnika.

graph = {0: [1, 3], 1: [0, 2, 3], 2: [4, 1, 5], 3: [4, 0, 1], 4: [2, 3, 5], 5: [4, 2]}
print("The adjacency List representing the graph is:")
print(graph)
print(graph.keys())
print(graph.values())

--------------------------

Nacrtati primer neusmerenog i usmerenog grafa (directed graph - DiGraph)

pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
print(type(G))
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()

G = nx.DiGraph()
print(type(G))
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()

-----------------------------------------------

Kreirati graf iz zadatog rečnika

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict


def make_graph_from_dict(g: Dict):
    G = nx.Graph()
    nodes = []
    graph_edges = []
    for i in g.keys():
        nodes.append(i)
        for j in g[i]:
            graph_edges.append((i, j))
    G.add_nodes_from(nodes)
    G.add_edges_from(graph_edges)
    return G


graph = {0: [1, 3], 1: [0, 2, 3], 2: [4, 1, 5], 3: [4, 0, 1], 4: [2, 3, 5], 5: [4, 2]}

G = make_graph_from_dict(graph)
nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()

--------------------------------------------------------------------------------

Obilazak grafa: pretragom u dubinu (dfs) obići sve njegove čvorove

import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()

def dfs(g,source,visited):
    print(source, end="->")
    visited.append(source)
    for i in g[source]:
        if i not in visited:
            dfs(g,i,visited)

dfs(G,1,[])

--------------------------------------------------------------------------------

Obilazak grafa (kreiranog iz rečnika): pretragom u dubinu (dfs) obići sve njegove čvorove


import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict


def make_graph_from_dict(g: Dict):
    G = nx.Graph()
    nodes = []
    graph_edges = []
    for i in g.keys():
        nodes.append(i)
        for j in g[i]:
            graph_edges.append((i, j))
    G.add_nodes_from(nodes)
    G.add_edges_from(graph_edges)
    return G


graph = {0: [1, 3], 1: [0, 2, 3], 2: [4, 1, 5], 3: [4, 0, 1], 4: [2, 3, 5], 5: [4, 2]}
print(graph)
G = make_graph_from_dict(graph)
nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()

# Rekurzivno rešenje

def dfs(g, source, visited):
    print(source, end="->")
    visited.append(source)
    for i in g[source]:
        if i not in visited:
            dfs(g, i, visited)


dfs(graph, 0, [])
print()
dfs(G, 0, [])
print()


# Iterativno resenje

def dfs(graph, source):
    S = list()
    visited_vertices = list()
    S.append(source)
    visited_vertices.append(source)
    while S:
        vertex = S.pop()  # skida sa vrha steka
        print(vertex, end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                S.append(u)
                visited_vertices.append(u)


print("DFS traversal of graph with source 0 is:")
dfs(graph, 0)

--------------------------------------------------------------------------------

Obilazak grafa (kreiranog iz rečnika): pretragom u širinu (bfs) i pretragom u dubinu (dfs) obići sve njegove čvorove

import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()


def bfs(graph, source):
    Q = Queue()
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({source})
    while not Q.empty():
        vertex = Q.get()
        print(vertex, end="--->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.update({u})


bfs(G, 1)
print()
bfs(G, 9)
print()
bfs(G, 2)
print()

# ovde nema izlaza pošto svaki graf ima susede
# pa moramo da ubacimo skup sa vec posecenima
# ili da koristimo usmeren graf
'''def dfs(graph, source):
    if(source is not None):
        print(source)
        for u in graph[source]:
            dfs(graph,u)'''


def dfs(graph, source, visited):
    if (visited is None):
        visited = set()
    visited.add(source)
    print(source, end="-->")
    for u in graph[source]:
        if (u not in visited):
            dfs(graph, u, visited)


dfs(G, 1, None)
print()
dfs(G, 9, None)
print()
dfs(G, 2, None)
print()

--------------------------------------------------------------------------------

Pronaći najkraće rastojanje između svih čvorova u grafu (verzija 1)

import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='y', node_size=800)

plt.show()


def dfs4(graph, source, visited, destination, mini):
    if visited is None:
        visited = list()
    visited.append(source)
    if source == destination:
        # print(visited)
        mini[0] = min(len(visited), mini[0])
    for u in graph[source]:
        if u not in visited:  # ako smo u ciklusu gde su svi poseceni nema poziva
            dfs4(graph, u, visited, destination, mini)
    visited.remove(source)  # kada smo obradili svu decu brisemo roditelja
    return mini[0] - 1


print(dfs4(G, 1, None, 9, [len(G.nodes)]))
print()

print("source - dest - dist")
for i in vertices:
    for j in vertices:
        if i <= j:
            print("  ",i, "    ", j, "    ", dfs4(G, i, None, j, [len(G.nodes)]))
            
 
--------------------------------------------------------------------------------

Pronaći najkraće rastojanje između svih čvorova u grafu (verzija 2)

import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='y', node_size=800)

plt.show()

# Obilazak grafa od zadatog čvora source
'''def bfs(graph, source):
    Q = Queue()
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({source})
    while not Q.empty():
        vertex = Q.get()
        print(vertex, end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.update({u})


bfs(G, 1)
print()
bfs(G, 9)
print()
bfs(G, 2)
print()'''


# Najkrace rastojanje od source do svih ostalih cvorova
def bfs2(graph, source):
    distance = {k: 9999999 for k in list(graph.nodes)}
    Q = Queue()
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({source})
    while not Q.empty():
        vertex = Q.get()
        if vertex == source:
            distance[vertex] = 0
        #print(vertex, end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                if distance[u] > distance[vertex]:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    return distance


print()
for i in vertices:
    print(f"\n source = {i}", bfs2(G, i))
print()


--------------------------------------------------------------------------------

Kreirati heš tabelu.

import random

class intDict(object):
    """A dictionary with integer keys"""
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int. Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets] 
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey an int. Returns entry associated
        with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets] # vrednost za kljuc dictKey traži se u redu sa indeksom dictKey%self.numBuckets
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

D = intDict(29)  # heš tabela ima 29 redova (numBuckets = 29)
for i in range(20): # u nju se unosi 20 vrednosti (0,1,...,19) za pseudoslučajne ključeve iz opsega (0,100000)
#choose a random int between 0 and 10**5
    key = random.randint(0, 10**5)
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: #violates abstraction barrier
    print(' ', hashBucket)
    
kljuc = int(input("Unesi kljuc: "))    
while(kljuc!=-1):
    print(D.getValue(kljuc))
    kljuc = int(input("Unesi kljuc: ")) 

--------------------------------------------------------------------------------

Napisati rekurzivni program za pronalaženje Dedekindovih brojeva (3, 6, 20, 168, 7581, 7828354)

class Dedekind:

    def __init__(self,dubina,br_cifara) -> None:
        super().__init__()
        self.dubina = dubina
        self.br_cifara = br_cifara
        self.ukupno=0
        self.stat=[[]]
        self.__formirajStat()
        #print(stat)

    def __str__(self) -> str:
        return str(self.ukupno)

    def __uslovni(self,x):
        v=[]
        i=0
        while(x>0):
            if(x%2==1):
                v.append(2**i)
            i+=1
            x=x//2
        return v

    def __formirajStat(self):
        for i in range(1,2**(self.dubina - 1)):
            self.stat.append([])
            v = self.__uslovni(i)
            self.stat[i]=[0]*len(v)
            for j in range(len(self.stat[i])):
                self.stat[i][j]=i-v[j]

    def dedekind(self,preth,i,dub,prenos):
        if(dub==self.dubina):
            return
        if(i==prenos):
            if(len(preth)==2**(self.dubina-1)):
                self.ukupno += 1
            self.dedekind(preth,0,dub+1,len(preth))
            return
        m=0
        if(len(preth)>0):
            mesta = self.stat[len(preth)]
            for p in range(len(mesta)):
                if(m<int(preth[mesta[p]])):
                    m=int(preth[mesta[p]])
        for k in range(m,br_cifara):
            pom = preth
            pom += str(k)
            self.dedekind(pom,i+1,dub,prenos)

if __name__=="__main__":
    dubina = 6
    br_cifara = 3
    d = Dedekind(dubina,br_cifara)
    d.dedekind("", 0, 0, 1)
    print(d)