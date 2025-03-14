def is_balanced(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []
        
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Further Exploration

def is_balanced(string):
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)
        elif char == ')':
            if stack == [] or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif char == ']':
            if stack == [] or stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif char == '}':
            if stack == [] or stack[-1] != '{':
                return False
            else:
                stack.pop()

    return stack == []

print(is_balanced("[]{}()") == True)
print(is_balanced("([{}]{}[])") == True)
print(is_balanced("([]{)") == False)
print(is_balanced(")]}{[()") == False)
print(is_balanced("(){[}]") == False)