# Two number sum

## Description:
A function that take in a non-empty array of distinct integers
and an integer representing a target sum. If any two numbers 
in the input array sum up to the target sum, the function should
return then in an array, in any order. 
If no two numbers sum up to the target sum, 
the function should return an empty array.

Parameters:
array <list>: list of integers
targetSum <integer>: integer representing a target sum

Return:
Interger pair which sum is equal to targetSum
empty otherwise
---

In the [original solution](https://github.com/ivanovitchm/datastructure/blob/main/lessons/week_03/twonumbersum.ipynb), 
we need two for's loops to travel the array. 
It works, but the time complexity of this algorithm is O(n^2). So
the objective is to solve this problem by reducing the time complexity 
to O(n) instead O(n^2). 

I solved this using Python dictionaries. first, i initalize an empty dicionary.
Then, in a single for loop, i called y the targetSum (te number that we want to verify if
it exists in the array) subtracted to the current value in the array that we were iteracting. If this value (y)
are not in the dictionary we append the current value from the vector into the dicionary, otherwise, we return the pair that reach the targetSum. This reduces the complexity from O(n^2) to O(n) because now we have only
a single for loop, so in the worst case we'll only do n interactions :smiley:. Furthermore, the step to verify
if a value exists in a dictionary is an operation that, in terms of time complexity is O(1).:smiley::smiley::smiley:

But what about the "space complexity"? :hushed:
