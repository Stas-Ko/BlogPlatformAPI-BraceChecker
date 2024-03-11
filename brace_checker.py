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
                return False, i  # Возвращает False и индекс неправильной скобки
    if stack:
        return False, stack[0][1]  # Возвращает индекс первой непарной скобки
    return True, -1  # Все скобки правильные

# Пример использования функции
print(is_valid_parentheses("{[]}"))  # (True, -1)
print(is_valid_parentheses("{[}]"))  # (False, 2)
