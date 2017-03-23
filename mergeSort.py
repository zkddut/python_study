#merge sort example code
a = [1,2,3,5] #sorted list
b = [2,4,7] #sorted list

m, n, i, j, res = len(a), len(b), 0, 0, []
while i < m and j < n:
  if a[i] < b[j]:
    res.append(a[i])
    i += 1
  else:
    res.append(b[j])
    j += 1
print(res)
#[1, 2, 2, 3, 4, 5]
