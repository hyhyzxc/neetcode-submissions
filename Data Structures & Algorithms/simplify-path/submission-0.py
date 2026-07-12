class Solution:
    def simplifyPath(self, path: str) -> str:
        # how to get a directory:
        # if encounter slash, skip till your next char is not a slash
        # then jump until your next char is a slash
        # extract this -> append it to a stack

        # if extracted and see that the contents is a .. 
        # pop the stack

        # if extracted and see that the contents is a .
        # continue

        l, r = 0, 0
        stack = []

        while r < len(path):
            while l < len(path) and path[l] == '/':
                l += 1
            
            r = l
            while r < len(path) and path[r] != '/':
                r += 1
            
            if l >= len(path) and r >= len(path):
                break
            
            directoryName = path[l: r]
            l = r

            if directoryName == '.':
                continue
            elif directoryName == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directoryName)
        
        return '/' + '/'.join(stack)
            
        