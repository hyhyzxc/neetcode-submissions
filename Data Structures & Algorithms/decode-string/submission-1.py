class Solution:
    def decodeString(self, s: str) -> str:
        #2[a3[b]]c
        # -> 2[abbb]c
        # -> abbbabbbc

        # axb3[z]4[c]
        # -> axbzzzzcccc

        # {2, [, a, bbb ]}

        # if number: append to stack
        # if open bracket: append to stack
        # if character: append to stack
        # if close bracket: pop until get open bracket, whatever is popped is the string.
        # -> pop again to get number
        # -> repeat the string by X times ( X = number popped )
        # -> append this new string to stack
        # -> join all elements in the stack

        stack = []
        i = 0

        while i < len(s):
            if s[i] == ']':
                characters = []
                while stack and stack[-1] != '[':
                    characters.append(stack.pop())
                stack.pop()

                word = ''.join(reversed(characters))

                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                
                multiplier = int(''.join(reversed(multiplier)))
                stack.append(multiplier * word)
            else:
                stack.append(s[i])
            i += 1
        
        return ''.join(stack)



        