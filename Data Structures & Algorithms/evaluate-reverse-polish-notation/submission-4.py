class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #i failed the first 2 times because i didn't
        # understand the notation due to the ambiguity
        # in the question, thanks a lot 👍
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[0]