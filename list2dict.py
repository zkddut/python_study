# below code is an example to convert a list to dict.
# It do not need to use if condition to check if we have key in dict
h = {}
l = [1,2,3,1,2]

for i, n in enumerate(l):
	h[n] = h.get(n, []) + [i]

print(h)
#{1: [0, 3], 2: [1, 4], 3: [2]}

h = {}
for i, n in enumerate(l):
	h[n] = h.get(n, 0) + 1

print(h)
#{1: 2, 2: 2, 3: 1}
