def main():
    conversion = input("What's your deal? ")
    print(convert(conversion))

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()