class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op in ['+', '-', '/', '*']:

                b = stack.pop()
                a = stack.pop()

                if op == '+':
                    res = a + b
                elif op == '-':
                    res = a - b
                elif op == '/':
                    res = int(a / b)
                elif op == '*':
                    res = a * b
                
                stack.append(res)

            else:
                stack.append(int(op))
            
        return stack[0]