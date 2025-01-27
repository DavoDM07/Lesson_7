#Write a Python function that takes two sets as input and returns a new set containing
#elements that are present in either of the input sets, but not in both
set1 = set('')
set2 = set('')
set1 = set(input())
set2 = set(input())
print(set1 ^ set2)