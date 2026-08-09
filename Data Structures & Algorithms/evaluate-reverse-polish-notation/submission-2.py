class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        stack = []
        i = 0
        res = 0
        while i < len(tokens):
            if tokens[i] not in op_map:
                stack.append(tokens[i])
                i += 1
                continue

            op2 = int(stack.pop())
            op1 = int(stack.pop())
            operand = tokens[i]
            res = op_map[operand](op1, op2)
            stack.append(res)
            i += 1

        return int(stack.pop())