conversions = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    "F": 5000,
    "G": 10000,
    "H": 50000,
}

roman_format = ["", "1", "11", "111", "12", "2", "21", "211", "2111", "13"]
valid_operators = ["+", "-", "*", "x", "X", "/", "e"]


def to_roman(num):
    count = 0
    output = ""
    my_str = str(num)
    roman_numerals = list(conversions.keys())
    for i in range(len(my_str) - 1, -1, -1):
        output = roman_format[int(my_str[i])].replace("1", roman_numerals[count]).replace("2", roman_numerals[
            count + 1]).replace("3", roman_numerals[count + 2]) + output
        count += 2
    return output


def to_arabic(roman_number):
    sum = 0
    for i in range(len(roman_number)):
        if i == len(roman_number) - 1 or conversions.get(roman_number[i]) >= conversions.get(roman_number[i + 1]):
            sum += conversions.get(roman_number[i])
        else:
            sum -= conversions.get(roman_number[i])
    return sum


def get_number_type(input_str):
    if input_str.isdigit():
        return "Arabic"
    validRomanNumeral = True
    validLetters = list(conversions.keys())
    for i in input_str:
        if validLetters.count(i) == 0:
            validRomanNumeral = False
    if validRomanNumeral:
        return "Roman"
    else:
        return "Incorrect"


def prepare_input(input):
    if get_number_type(input) == "Arabic":
        num = int(input)
    elif get_number_type(input) == "Roman":
        num = to_arabic(input)
    else:
        return "False input"
    return num


def get_inputs():
    first_num = prepare_input(input("Type your first number here\n"))
    operator = input("Type your operator here\n")
    second_num = prepare_input(input("Type your second number here\n"))
    return first_num, operator, second_num


print("Welcome to my Roman Numeral calculator!")
print("You type two numbers, and an operator, and it will give you the result")
print("Inputs can be in Roman or Arabic numerals, but the output will always be in Roman")
print("Note that Roman Numerals only scale to 3999, so I have added F, G, and H to extend this scale")
while input('Type "Start" to begin, anything else to stop\n').upper() == "START":
    first, operator, second = get_inputs()

    if first == "False input" or second == "False input" or valid_operators.count(operator) == 0:
        print("You have given an improper input")
    else:
        first_roman = to_roman(first)
        second_roman = to_roman(second)
        if operator == "+":
            print(first_roman, "+", second_roman, "=", to_roman(first + second))
        elif operator == "-":
            print(first_roman, "-", second_roman, "=", to_roman(first - second))
        elif operator == "*" or operator == "x" or operator == "X":
            print(first_roman, "x", second_roman, "=", to_roman(first * second))
        elif operator == "/":
            print(first_roman, "/", second_roman, "=", to_roman(int(first / second)))
        elif operator == "e":
            print(first_roman, "e", second_roman, "=", to_roman(first ** second))
        else:
            print("How did we get here?")
