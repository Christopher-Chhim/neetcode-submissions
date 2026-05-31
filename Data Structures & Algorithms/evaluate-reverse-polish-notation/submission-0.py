class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                operator1 = stack.pop()
                operator2 = stack.pop()

                if i == "+":
                    stack.append(operator2 + operator1)
                elif i == "-":
                    stack.append(operator2 - operator1)
                elif i == "/":
                    stack.append(int(operator2 / operator1))
                elif i == "*":    
                    stack.append(operator2 * operator1)
            else:
                stack.append(int(i))
        return stack[0]