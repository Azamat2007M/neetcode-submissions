class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if "+" == t:
                stack.append(stack.pop() + stack.pop())
            elif '-' == t:
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif '*' == t:
                stack.append(stack.pop() * stack.pop())
            elif '/' == t:
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        
        return stack.pop()

        #Another method with lambda
        # operators = {"+": lambda a,b: a+b,
        #             "-": lambda a,b: a-b,
        #             "*": lambda a,b: a*b,
        #             "/": lambda a,b: int(a/b),}

        # stack = []
        # for token in tokens:
        #     operator = operators.get(token)

        #     if operator is not None:
        #         a = stack.pop()
        #         b = stack.pop()
        #         stack.append(operator(b,a))
        #     else:
        #         stack.append(int(token))
        
        # return stack.pop()