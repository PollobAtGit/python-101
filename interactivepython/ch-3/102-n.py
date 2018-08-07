from Stack import Stack

def parenthesis_checker(equation):

    if equation:
    
        internal_stack = Stack()
        
        for ch in equation:
            if ch == "(":
                internal_stack.push(ch)
            elif ch == ")":
                if internal_stack.empty():
                    return False

                internal_stack.pop()
        
        return internal_stack.empty() 

def parenthesis_checker_two(equation):

    stack = Stack()

    for symbol in equation:
        if symbol in "({[":
            stack.push(symbol)
        elif symbol in ")}]":

            if stack.empty(): 
                return False
            
            last_symbol_complement_brace = get_complement_brace(stack.pop())

            is_balanced = symbol == ")" and last_symbol_complement_brace == ")" \
                        or symbol == "}" and last_symbol_complement_brace == "}" \
                            or symbol == "]" and last_symbol_complement_brace == "]"
            
            if not is_balanced:
                return False

    return stack.empty()


def get_complement_brace(symbol):
    if symbol == "(": return ")"
    if symbol == "{": return "}"
    if symbol == "[": return "]"

"""
print(parenthesis_checker("(())"))
print(parenthesis_checker(")(())"))
print(parenthesis_checker("))"))
print(parenthesis_checker(""))
print(parenthesis_checker(None))
print(parenthesis_checker("()()"))
print(parenthesis_checker("())("))
"""

print(parenthesis_checker_two("{{([][])}()}"))
print(parenthesis_checker_two("[[{{(())}}]]"))
print(parenthesis_checker_two("[][][](){}"))

print(parenthesis_checker_two("}[][][](){}"))

print(parenthesis_checker_two("( [ ) ]"))
print(parenthesis_checker_two("( ( ( ) ] ) )"))
print(parenthesis_checker_two("[ { ( ) ]"))
