from Stack import Stack

def check_brackets_from_string(text):
    opening_brackets_stack = Stack()

    for char in text:

        if char in ['(','[','{']:
            opening_brackets_stack.push(char)
        elif char not in [')','}',']']:
            pass
        else:
            if opening_brackets_stack.size() > 0:

                peek = opening_brackets_stack.peek()
                opening_brackets_stack.pop()

                if peek == '(' and char != ')':
                    return False
                if peek == '{' and char != '}':
                    return False
                if peek == '[' and char != ']':
                    return False
            else:
                return False

    if opening_brackets_stack.empty():
        return True

    return False
