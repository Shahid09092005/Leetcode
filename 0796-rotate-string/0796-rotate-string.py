class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        goal+=goal
        if(s in goal):
            return True
        return False
        