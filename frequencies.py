"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if frequencies.get(str(item)) == None:
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] = frequencies.get(str(item)) + 1
    # Your code goes here
    return frequencies
