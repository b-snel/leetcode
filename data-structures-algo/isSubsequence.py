class Solution:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def isSubsequence(s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)



s = 'pork'
t = 'puppy'
if(Solution.isSubsequence(s, t)):
    print("yippee")