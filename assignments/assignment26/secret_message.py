#Author: Logan Simonis
def to_symbols(message):
    print("Your encoded message is: ", end="")
    for letter in message:
        print(str(ord(letter)) + ".", end="")
    print("")

def to_letters(symbols):
    print("Your decoded message is: ", end="")
    symbols.split(".")
    for symbol in symbols:
        if symbol.isdigit():
            print(chr(int(symbol.strip())), end="")
        else:
            print(" ", end="")
    print("")

print("Secret Messages!")
while True:
    command = input("(E)ncode, (D)ecode, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "e":
        message = input("Enter a secret message: ").strip().lower()
        to_symbols(message)
    elif command == "d":
        symbols = input("Enter an encoded message: ").strip().lower()
        to_letters(symbols)
    else:
        print("Invalid Command!")
print("Goodbye")