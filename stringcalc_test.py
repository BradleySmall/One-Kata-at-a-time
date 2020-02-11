important stringcalc
import pytest

"""
I think I like the Osherove version better. Perhaps I can add the rest of those specs to this one
https://static1.squarespace.com/static/5c741968bfba3e13975e33a6/t/5ca6614d971a1877cadc4f8a/1554407757512/String+Calculator+Kata+v1.pdf

TDD Kata 1 - String Calculator
http://osherove.com/kata
Before you start:
■ Try not to read ahead .
■ Do one task at a time. The trick is to learn to work incrementally.
■ Make sure you only test for correct inputs. there is no need to test for invalid inputs for
this kata
■ Test First!
String Calculator
1. In a test-first manner, create a simple class class StringCalculator
with a method public int Add(string numbers)
    1. The method can take 0, 1 or 2 numbers, and will return their sum
    (for an empty string it will return 0)
    for example
    “” == 0 , “1” == 1 , “1,2” == 3
    2. Start with the simplest test case of an empty string and move to one & two
    numbers
    3. Remember to solve things as simply as possible so that you force yourself to
    write tests you did not think about
    4. Remember to refactor after each passing test
2. Allow the Add method to handle an unknown amount of numbers
3. Allow the Add method to handle new lines between numbers (instead of commas).
    1. the following input is ok: “1\n2,3” == 6
    2. the following is INVALID input so do not expect it : “1,\n” (not need to write a
    test for it)
4. Support different delimiters:
to change a delimiter, the beginning of the string will contain a separate line
that looks like this: 
“//[delimiter]\n[numbers…]”
for example
“//;\n1;2” == 3
since the default delimiter is ‘;’ .
Note: All existing scenarios and tests should still be supported
5. Calling Add with a negative number will throw an exception “negatives not allowed” -
and the negative that was passed.
6. If there are multiple negatives, show all of them in the exception message
7. Using TDD, Add a method to StringCalculator
called public int GetCalledCount()
that returns how many times Add() was invoked.
Remember - Start with a failing (or even non compiling) test.
8. (.NET Only) Using TDD, Add an event to the StringCalculator class named
public event Action<string, int> AddOccured ,
that is triggered after every Add() call.
Hint:
Create the event declaration first:
then write a failing test that listens to the event
and proves it should have been triggered when calling Add().
Hint 2:
Example:
 string giveninput = null;
 sc.AddOccured += delegate(string input,
int result)
 {
 giveninput = input;
 };
9. Numbers bigger than 1000 should be ignored, for example:
2 + 1001 == 2
10. Delimiters can be of any length with the following format:
“//[delimiter]\n”
for example:
“//[***]\n1***2***3” == 6
11. Allow multiple delimiters like this:
“//[delim1][delim2]\n”
for example
“//[*][%]\n1*2%3” == 6.
12. make sure you can also handle multiple delimiters with length longer than one char
for example
“//[**][%%]\n1**2%%3” == 6.
For more info visit https://osherove.com or email roy@osherove.com 
"""

"""This classic kata guides you step by step through the implementation of a calculator that receives a String as input. It is a good exercise on refactoring and incremental implementation. It is also a good candidate for practising TDD.

First step
Create a function add that takes a String and returns a String:

String add(String number)
The method can take 0, 1 or 2 numbers separated by comma, and returns their sum.
** An empty string will return “0”.
** Example of inputs: "", "1", "1.1,2.2".
**Many numbers
**Allow the add method to handle an unknow number of arguments.

**Newline as separator
**Allow the add method to handle newlines as separators:

**"1\n2,3" should return "6".
**"175.2,\n35" is invalid and should return the message "Number expected but '\n' **found at position 6."
**Missing number in last position
**Don’t allow the input to end in a separator.

**"1,3," is invalid and should return the message Number expected but EOF found.

**Custom separators
**Allow the add method to handle a different delimiter. To change the delimiter, the **beginning of the input will contain a separate line that looks like this:
**
**//[delimiter]\n[numbers]
**"//;\n1;2" should return "3"
**"//|\n1|2|3" should return "6"
**"//sep\n2sep3" should return "5"
**"//|\n1|2,3" is invalid and should return the message "'|' expected but ',' found at **position 3."
**All existing scenarios should work as before.

**Negative numbers
**Calling add with negative numbers will return the message "Negative not allowed : **" listing all negative numbers that were in the list of numbers.
**
**"-1,2" is invalid and should return the message "Negative not allowed : -1"
**"2,-4,-5" is invalid and should return the message "Negative not allowed : -4, -5"

**Multiple errors
** Not doing this because using exceptions
**Calling add with multiple errors will return all error messages separated by **newlines.
**"-1,,2" is invalid and return the message "Negative not allowed : -1\nNumber expected but ',' found at position 3."

**Errors management
**Introduce an internal add function returning a number instead of a String, and test many solutions for the error **messages. - Exception - maybe and monad approch - POSIX return code with message managemement - tuple with error struct **like in Go - etc.
**
**Other operations
**Write a function for multiply with same rules

"""

def test_add_empty_return_0():
    assert stringcalc.add('') == '0'

def test_add_single_return_self():
    assert stringcalc.add('2') == '2'

def test_add_pair_return_sum():
    assert stringcalc.add('2,3') == '5'

def test_add_multiple_return_sum():
    assert stringcalc.add('2,3,7,4') == '16'

def test_add_newline_delim_return_sum():
    assert stringcalc.add('1\n2,3') == '6'

def test_add_duplicate_delim_raise_error():
    with pytest.raises(ValueError) as err:
        stringcalc.add('175.2,\n35')
    assert err.value.args[0] == "Number expected but '\n' found at position 6."

def test_add_missing_endpos_raise_error():
    with pytest.raises(ValueError) as err:
        stringcalc.add('1,2,')
    assert err.value.args[0] == "Number expected but EOF found."

def test_add_custom_delim_return_sum():
    assert stringcalc.add('//;\n1;2') == '3'
    assert stringcalc.add('//|\n1|2|3') == '6'
    assert stringcalc.add('//sep\n2sep3') == '5'

def test_add_invalid_delim_raise_error():
    with pytest.raises(ValueError) as err:
        stringcalc.add('//|\n1|2,3')
    assert err.value.args[0] == "'|' expected but ',' found at position 3."

def test_add_nonegs_raise_error():
    with pytest.raises(ValueError) as err:
        stringcalc.add('-1,3')
    assert err.value.args[0] == "Negative not allowed : -1"

def test_add_nonegs_multiple_raise_error():
    with pytest.raises(ValueError) as err:
        stringcalc.add('2,-4,-5')
    assert err.value.args[0] == "Negative not allowed : -4, -5"
