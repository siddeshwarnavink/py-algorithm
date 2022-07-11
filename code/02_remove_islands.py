"""
Problem:
We are given a black&white image which is represented by a matrix with 0 representing black pixle 
and 1 representing white pixle. Our objective is to remove the black pixles which are not linked to the
border. These black pixles that forms 'island' has to be removed.

Sample input: 
[
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

Sample output:
[
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

(Source: https://www.youtube.com/watch?v=4tYoVx0QoN0)
"""