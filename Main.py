def encode_password(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

encoded_password = None
decoded_password = None

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = input("Please enter an option: ")

    if option == '1':
        if decoded_password is None:
            user_response = input("Please enter your password to decode:")
            encoded_password = encode_password(user_response)
            print("Your password has been stored and encoded!\n")
        else:
            print(f"The decoded password is {encoded_password}, and the original password is {user_response2}\n")

    elif option == '2':
        if encoded_password is None:
            user_response2 = input("Please enter your password to decode: ")
            decoded_password = decode_password(user_response2)
            print("Your password has been decoded and stored!\n")
        else:
            print(f"The encoded password is {encoded_password}, and the original password is {user_response}\n")

    elif option == '3':
        break

    else:
        print("Invalid option. Please choose a valid option (1, 2, or 3).")
