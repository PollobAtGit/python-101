class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s:

            def is_operand(y):
                if ord(y) >= 48 and ord(y) <= 57:
                    return True
                return False

            operator_stack = []
            operand_stack = []

            operators = [str(x) for x in "+-"]
            start_braces = "("
            end_braces = ")"

            if not [True for x in operators if x in s]:
                s = s.replace(start_braces, "").replace(end_braces, "")# (1), (2) => valid operations
                if int(s) != int(str(int(s))):
                    return s
                return int(s)

            def calculate_on_data():

                while len(operator_stack) != 0 and operator_stack[-1] not in start_braces:

                    operator = operator_stack.pop()

                    if len(operand_stack) >= 2:
                        operand_one = operand_stack.pop()
                        operand_two = operand_stack.pop()

                        is_next_operator_minus = True if len(operator_stack) != 0 and operator_stack[-1] == "-" else False

                        if not is_next_operator_minus:
                            if operator in "+":
                                operand_stack.append(int(operand_one) + int(operand_two))
                            else:
                                operand_stack.append(int(operand_two) - int(operand_one))
                        else:
                            operand_stack.append((-1 * int(operand_one)) + int(operand_two))

                if len(operator_stack) != 0:
                    operator_stack.pop()

            i = 0
            while i < len(s):
                if s[i] in [start_braces] + operators:
                    operator_stack.append(s[i])
                if is_operand(s[i]):

                    num = s[i]

                    i = i + 1
                    while i < len(s) and is_operand(s[i]):
                        num = num + s[i]
                        i = i + 1

                    operand_stack.append(int(num))
                    continue

                if s[i] in end_braces:
                    calculate_on_data()

                i = i + 1

            if len(operator_stack) != 0 and len(operand_stack) != 0:
                calculate_on_data()

            return operand_stack[0]


s = Solution()

print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
print(s.calculate("1+1"))
print(s.calculate("2-1+2"))# 3

print(s.calculate("0"))# 3

print(s.calculate("2147483647"))# 3
print(s.calculate("(1+1)"))# 3
print(s.calculate("(1)"))# 3
print(s.calculate("1-11"))# 3
