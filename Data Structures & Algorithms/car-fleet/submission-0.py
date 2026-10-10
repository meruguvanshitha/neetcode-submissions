class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Pair position and speed, sort by position in reverse (closest to target first)
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in pairs:
            # Calculate time to reach the target: (target - current_position) / speed
            time = (target - p) / s
            stack.append(time)
            
            # If the car behind catches up to the car ahead, they form a single fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)