class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    from collections import OrderedDict
    def repeatedNumber(self, lst):
        n = len(lst)
        lst1 = []
        su = sum(lst)
        dicti = {}
        for i in lst:
            if i not in dicti:
                dicti[i] = 1
            else:
                dicti[i] += 1

        for i in dicti:
            if dicti[i] == 2:
                ans = i
                break

        suans = su - ans
        ans1 = (n * (n + 1)) // 2 - suans
        lst1.append(ans)
        lst1.append(ans1)
        return lst1
