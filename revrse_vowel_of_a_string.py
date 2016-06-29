#Givin s = "leetcode", return "leotcede"

class Solution(object):
  def reverseVowels(self, s):
    """
    : tyte s : str
    : rtype : str
    """
    vowels = []
    s_list = list(s)
    for i in range(0, len(s_list)):
      count = 0
      if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
        for j in range(count, len(s_list)):
          if s_list[len(s_list)-j-1] in ['a','e','i','o','u','A','E','I','O','U']:
            s_list[len(s_list)-j-1],s_list[i] = s_list[i],s_list[len(s_list)-j-1]
            count = j
            break;
      if i >= count:
        break;

    str = "".join(s_list)

    return str

a = Solution()
print a.reverseVowels("abcdeABCDE")

