class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } # dictionary mapping close -> open

        for c in s: # go through 1 char at a time
            if c in closeToOpen: # if char is opening bracket
                if stack and stack[-1] == closeToOpen[c]: # checks if stack exists / and top of stack (last element) matches correct opening bracket for this closing bracket
                    stack.pop() # removes opening bracket
                else:
                    return False # stack is empty / top of stack doesn't match
            else:
                stack.append(c) # if c is opening bracket push onto stack

        return True if not stack else False