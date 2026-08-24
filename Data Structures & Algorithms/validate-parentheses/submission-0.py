class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        o = {"(":")" , "[" :"]" , "{" : "}"}

        for c in s:
            if c in o:
                stack.append(c)

            else:
                if not stack or o[stack.pop()] != c:
                    return False
                    
        return len(stack)==0                  