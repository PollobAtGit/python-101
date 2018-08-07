from Stack import Stack

def decimal_to_other_base(num, base):
    
    if base and base < 10:
        internal_stack = Stack()

        while num > 0:
            internal_stack.push(num % base)
            num = int(num / base)

        ret = []
        while not internal_stack.empty():
            ret.append(internal_stack.pop())
        
        return "".join([str(x) for x in ret])

def decimal_to_hexa(num):
    
    if num:
        hex_base = 16

        internal_stack = Stack()

        while num > 0:
            internal_stack.push(to_hex_symbol(num % hex_base))
            num = int(num / hex_base)

        ret = []
        while not internal_stack.empty():
            ret.append(internal_stack.pop())

        return "".join([str(x) for x in ret])

def to_hex_symbol(digit):

    if digit < 10: return digit
    if digit < 16:
        other_symbols = "ABCDEF"
        return other_symbols[digit - 10]


def decimal_to_twenty_six(num):
    
    if num:
        twenty_six_base = 26

        internal_stack = Stack()

        while num > 0:
            internal_stack.push(to_twenty_six_symbol(num % twenty_six_base))
            num = int(num / twenty_six_base)

        ret = []
        while not internal_stack.empty():
            ret.append(internal_stack.pop())

        return "".join([str(x) for x in ret])

def to_twenty_six_symbol(digit):

    if digit < 10: return digit
    if digit < 26:
        other_symbols = "ABCDEFGHIJKLMNOPQ"
        return other_symbols[digit - 10]