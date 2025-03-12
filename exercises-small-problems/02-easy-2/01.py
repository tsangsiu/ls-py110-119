def pad_zeroes(num):
    num_str = str(num)

    if len(num_str) < 2:
        return f'0{num_str}'
    else:
        return num_str

def dms(angle_float):
    angle_float %= 360

    angle_degree, angle_float = divmod(angle_float, 1)
    angle_minute, angle_float = divmod(angle_float * 60, 1)
    angle_second, angle_float = divmod(angle_float * 60, 1)

    angle_dms = f'{int(angle_degree)}\u00B0' + \
                f"{pad_zeroes(int(angle_minute))}'" + \
                f'{pad_zeroes(int(angle_second))}"'

    return angle_dms

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"