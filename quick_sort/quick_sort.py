class Solution(object):
  def partition(self, A, lo, hi):
    p = A[hi]
    i = lo
    for j in range(lo, hi ):
      if A[j] <= p :
        A[i], A[j] = A[j], A[i]
        i = i + 1
    A[i], A[hi] = A[hi], A[i]
    return i

  def quick_sort(self, A, lo, hi):
    if lo < hi:
      p = self.partition(A, lo, hi)
      self.quick_sort(A, lo, p-1)
      self.quick_sort(A, p+1, hi)

 
a = Solution()
A = [21,4, 1, 3, 9, 20, 25, 6, 21, 14]
a.quick_sort(A,0,len(A)-1)
print A
