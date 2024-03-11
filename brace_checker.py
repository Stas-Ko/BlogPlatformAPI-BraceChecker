def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for i, char in enumerate(s):
        if char in mapping.values():
            stack.append((char, i))
        elif char in mapping.keys():
            if stack and stack[-1][0] == mapping[char]:
                stack.pop()
            else:
                return False, i  # Returns False and the index of the incorrect parenthesis
    if stack:
        return False, stack[0][1]  # Returns the index of the first unpaired parenthesis
    return True, -1  # All parentheses are correct

# Example of using the function
print(is_valid_parentheses("{[]}"))  # (True, -1)
print(is_valid_parentheses("{[}]"))  # (False, 2)
