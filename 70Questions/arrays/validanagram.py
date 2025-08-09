# Hash Map method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sorted method (simple) uses less memory and could be more efficent
        return sorted(s) == sorted(t)

        if len(stringT) != len(stringS):
            return False
        stringT, stringS = {}, {}

        for i in range(len(s)):
            stringS[s[i]] = 1 + stringS.get(s[i], 0)
            stringT[t[i]] = 1 + stringT.get(t[i], 0)
        for c in stringS:
            if stringS[c] != stringT[c]:
                return False

        return True
