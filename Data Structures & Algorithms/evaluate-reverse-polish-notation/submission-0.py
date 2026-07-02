class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            # If token is an operator
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:  # division
                    result = int(a / b)  # truncate toward zero

                stack.append(result)
            else:
                # Token is a number
                stack.append(int(token))

        return stack[0]