# Assignment 1

## Libraries
No libraries are used for any of these Problems.

## Python version
This program runs on version 3.9.1.

## Usage
All problems will not print automatically. When calling the main function, you need to call a print to see the result.

### Problem 1:
Problem one takes a list "numbers" (an error will be printed if numbers is not a list) and returns True if the sequence of positive integers are all triangular numbers.

To call and print main function:
    print(trianglenos(numbers))


### Problem 2:
Problem two consists of two parts. Both parts take as parameters two separate lists of numbers: "list1" and "list2".

a) The first function, l_intersection, returns the set intersection of the two lists.

To call and print function:
    print(l_intersection(numbers))


b) The second function, l_union, returns the set union of the two lists.

To call and print main function:
    print(l_union(numbers))


### Problem 3:
Problem three takes a list "list1" (an error will be printed if numbers is not a list) and returns a new list. This new list indicates how many times each element in list1 occurrs, and it is sorted from greatest frequency to least.

To call and print main function:
    print(occurrences(list1))


### Problem 4:
Problem four takes a list "S" (an error will be printed if numbers is not a list) and returns a new list. This new list is the powerset of S- it includes every subset of the elements of St.

To call and print main function:
    print(powerset(S))


### Problem 5:
Problem five takes a list "S" and a list "Tau". It returns True if Tau is a finite topological space on S, and False otherwise. It works through multiple levels of checking:
1. Sort Tau to be in an order that allows for easier comparisons in later steps.
2. Ensure all digits of Tau are in the Powerset- here we also check for the simple set of [[],[S]] which is a valid topology.
3. Check to satisfy Requirement A- that Tau contains both [] and S.
4. Check to satisfy Requirement B- that for any U & V in Tau, Tau contains the intersection of U & V.
5. Check to satisfy Requirement C- that for any U & V in Tau, Tau contains the union of U & V.

To call and print main function:
    print(check_topology(S,Tau))