def maxPower(s):
    count = 1
    max_power = 1
    for indx in range(len(s) - 1):
        if s[indx] == s[indx + 1]:
            count += 1
        else:
            count = 1
        max_power = max(max_power, count)
    return max_power
