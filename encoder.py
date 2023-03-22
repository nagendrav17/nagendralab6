
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    user_option = int(input("Please enter an option:"))
    return user_option


def encode(user_password):
    encoded_password = []
    for n in user_password:
        new_n = int(n) + 3
        encoded_password.append(str(new_n))
    return "".join(encoded_password)

def decode(encoded_password):
    decoded_res = ''
    for char in encoded_password:
        char = int(char)
        char -= 3
        decoded_res += str(char)
    return decoded_res

def main():
    user_option = menu() # calls the menu and takes user_input
    while user_option != 3:
        if user_option == 1:
            user_password = input("Please enter your password to encode:")
            encode(user_password.strip())
            print()
            print("Your password has been encoded and stored!")
            print()

        if user_option == 2:
            encoded_password = encode(user_password)
            og_pw = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {og_pw}. ')

        user_option = menu()
    else:
        exit()


if __name__ == '__main__':
     main()
