class Solution:
    def calPoints(self, operations: List[str]) -> int:
        v = []  # Initialize an empty list to keep track of the scores
        
        for i in operations:
            if i.lstrip('-').isdigit():  # If it's a number, convert and add it
                v.append(int(i))
            elif i == "+":  # Sum of the last two scores
                v.append(v[-1] + v[-2])
            elif i == "D":  # Double the last score
                v.append(v[-1] * 2)
            elif i == "C":  # Remove the last score
                v.pop()
                
        return sum(v)  # Return the total sum of all scores remaining