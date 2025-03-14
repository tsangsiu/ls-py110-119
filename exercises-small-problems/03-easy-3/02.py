'''

[P]
- Rules:
  - Explicit:
    - Write two functions that each take a time of day in 24 hour format,
      and return the number of minutes before and after midnight
    - Both functions should return a value in the range 0 through 1439
- Input: String representing a time of day in 24 hour format
- Output: Integer

[E]

[D]

[A]
- Implement the function `after_midnight` first
- Extract the hour and minute part from the string
- Turn them into integers
- Calculate the number of minutes after midnight by 60*hour + minute
- Return the result moduluo 24*60

- For the `before_midnight` function, pass the argument to `after_midnight`
- Calculate 24*60 - result moduluo 24*60
- Return the above result

'''

HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
MINUTES_IN_A_DAY = MINUTES_IN_AN_HOUR * HOURS_IN_A_DAY

def after_midnight(time):
    hour, minute = [int(part) for part in time.split(":")]
    return (MINUTES_IN_AN_HOUR * hour + minute) % MINUTES_IN_A_DAY

def before_midnight(time):
    return (MINUTES_IN_A_DAY - after_midnight(time)) % MINUTES_IN_A_DAY
    


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True