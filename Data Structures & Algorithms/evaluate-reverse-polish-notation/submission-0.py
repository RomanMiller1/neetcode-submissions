class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                self.stack.append(int(token))
            
            else:
                a = self.stack.pop()
                b = self.stack.pop()

                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                elif token == "/":
                    result = int(b / a)

                self.stack.append(result)
            
        return self.stack[-1]
            


        