#!/usr/bin/python
import math
input = '231832-767346'

def check_password(current, maximum):
    count = 0
    while current <= maximum:
        digits = [int(n) for n in str(current)]
        increase = [digits[i] <= digits[i + 1] for i in range(len(digits) - 1)]
        consecutive = [digits[i] == digits[i + 1] and (i == 0 or digits[i] != digits[i - 1]) and (i == len(digits) - 2 or digits[i] != digits[i + 2]) for i in range(len(digits) - 1)]
        # if False not in increase:
        #     print current, True in consecutive
        if False not in increase and True in consecutive:
            count += 1
        current += 1
    return count


def main():
    minimum, maximum = [int(input.split('-')[0]), int(input.split('-')[1])]
    print check_password(minimum, maximum)

if __name__ == "__main__":
   main()