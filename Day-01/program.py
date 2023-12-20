def main():
    with open("input.txt") as file:
        sum = 0
        for line in file.readlines():
            calibration_value = find_calibration_value(line)
            print(line.strip() + " = " + str(calibration_value))
            sum += calibration_value
        print("Sum of all calibration values: " + str(sum))

def find_calibration_value(line):
    first_digit = -1
    last_digit = -1
    for c in line:
        if c.isdigit():
            if first_digit == -1: first_digit = int(c)
            last_digit = int(c)
    return first_digit * 10 + last_digit



if __name__=="__main__":
    main()