l = [1, 2, 3]

subsets = []
for i in range(len(l)):
    for x in range(len(l)):
        subset = l[x:x+i]
        subsets.append(subset)

print(subsets)