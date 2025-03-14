'''

[P]
- Rules:
  - Explicit:
    - Write a function that takes a minute-based format with respect to midnight
      and return the time of day in 24-hour format
    - The function should work with any integer input
    - Before midnight: -ve
    - After midnight: +ve
- Input: Integer
- Output: String representing time in 24-hour format

[E]

[D]

[A]
- If the given minute (input) is not between 0
  and 60*24 (the number of minute in a day),
  - Add or minuus 60*24 until the number is in that range
- Find the quotient and remainder when the resultant number is divided by 60.
- The quotient is the hour, and the remainder is the minute
- Format the results in string, and in the format of 'HH:SS'
- Return the above string

'''

def time_of_day(minute):
    HOURS_IN_A_DAY = 24
    MINUTES_IN_AN_HOUR = 60
    MINUTES_IN_A_DAY = MINUTES_IN_AN_HOUR * HOURS_IN_A_DAY

    minute %= MINUTES_IN_A_DAY
    hour, min = divmod(minute, MINUTES_IN_AN_HOUR)

    return f'{hour:02d}:{min:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True