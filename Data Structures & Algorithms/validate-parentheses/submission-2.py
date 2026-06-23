class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ')':'(', 
            ']':'[', 
            '}':'{'
        }

        stack = []
        currIndex = 0
        strLength = len(s)

        while currIndex < strLength:
            currChar = s[currIndex]

            if currChar == '(' or currChar == '[' or currChar == '{':
                stack.append(currChar)

            else:
                if not stack or stack[-1] != bracketMap[currChar]:
                    return False
                
                stack.pop()
            
            currIndex += 1
        
        return len(stack) == 0




        