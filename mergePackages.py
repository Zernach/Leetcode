"""
Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.

Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Examples:

Input: items = [4, 6, 10, 15, 16], limit = 21
Output: [3, 1]
Explanation: The weight of the items at indices 3 and 1 sum up to the specified limit.
[execution time limit] 4 seconds (py3)

[input] array.integer items

A list of item weights.

[input] integer limit

The weight limit we're aiming for by merging two packages.

[output] array.integer

A pair of item indices indicating the two items that, when merged, reach the specified limit.
"""

def merge_packages(items, limit):

    for i1 in range(0, len(items)):
        for i2 in range(1, len(items)):
            if items[i1] + items[i2] == limit:
                return [i2, i1]
    return []
                