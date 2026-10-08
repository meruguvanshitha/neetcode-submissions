class Solution:
    def dailyTemperatures(self, t):
        r=[0]*len(t)
        s=[]
        for i,x in enumerate(t):
            while s and t[s[-1]]<x:
                j=s.pop()
                r[j]=i-j
            s.append(i)
        return r