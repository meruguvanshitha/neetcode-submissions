class Solution:
    def evalRPN(self, t: List[str]) -> int:
        s=[]
        for x in t:
            if x in '+-*/':
                b,a=s.pop(),s.pop()
                s+=[a+b if x=='+' else a-b if x=='-' else a*b if x=='*' else int(a/b)]
            else:s+=[int(x)]
        return s[0]