def repeater(string):
  output_string = ''
  for char in string:
      output_string = output_string + char + char
  return output_string

def repeater(string):
   return ''.join([char * 2 for char in string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True