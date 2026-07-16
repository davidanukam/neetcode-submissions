class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif len(token) > 1 and "-" in token:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-": 
                    stack.append(num1 - num2)
                elif token == "*": 
                    stack.append(num1 * num2)
                elif token == "/": 
                    stack.append(int(num1 / num2))
        return stack[-1] if len(stack) else 0
