def main():
    #prompt user for name variable
    case = input("What's your variable? ")
    output = replace(case)
    print(output)

def replace(case):
    # write the new word starting with the first character which is lowercase
    new_case = case[0].lower()
    # iterate through the string to find the uppercase letter starting from the second character
    for char in case[1:]:
    # include a _ before the uppercase letter and lowecase the uppercase letter
        if char.isupper():
            new_case += '_'
        new_case += char.lower()

    return new_case

main()