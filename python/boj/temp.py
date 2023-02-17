from itertools import permutations, combinations

a = [1,2,3]
permute = permutations(a,3)
combi = combinations(a, 3)
print(list(permute))
print(list(combi))