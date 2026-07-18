class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s)%2 != 0):
            return False
        
        stack = []

        for i in range(len(s)): 
            last_i = len(stack) - 1
            if last_i < 0:
                stack.append(s[i])
                continue
            
            if (s[i] == ')' and stack[last_i] == '(') or (s[i] == ']' and stack[last_i] == '[') or (s[i] == '}' and stack[last_i] == '{'): 
                stack.pop()
            else:
                stack.append(s[i])

        return True if len(stack) == 0 else False

        