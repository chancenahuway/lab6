# This program encodes and decodes an 8-digit password using a simple cypher.
# This is Lab 6 for COP 3502C, Summer 2023.
# This program was written by Dylan Dixon (decode) and Chance Nahuway (main/encode).


# This function takes in an 8-digit password (string), encodes it by shifting each digit up by
# 3 (e.g. 00009962 is encoded as 33332295), and returns the encoded password (string).
def encode(decoded_password):
    encoded_password = ""
    for character in decoded_password:
        encoded_password += str((int(character) + 3) % 10)
    return encoded_password


# This function takes in an 8-digit encoded password (string), decodes it by shifting each digit
# down by 3 (e.g. 33332295 is decoded as 00009962), and returns the decoded password (string).
def decode(encoded_password):
    # FIXME
    return decoded_password


if __name__ == '__main__':
    enc_pw = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        user_input = input("Please enter an option: ")
        if user_input == "1":
            orig_pw = input("Please enter your password to encode: ")
            enc_pw = encode(orig_pw)
            print("Your password has been encoded and stored!")
            print("")
        elif user_input == "2":
            if enc_pw is None:
                print("An original password must be encoded before it can be decoded.")
                print("")
                continue
            dec_pw = decode(enc_pw)
            print(f"The encoded password is {enc_pw}, and the original password is {dec_pw}.")
            print("")
        elif user_input == "3":
            break
        else:
            print("Your selection is invalid. Please enter 1, 2, or 3.")
            print("")
