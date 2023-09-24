import string

def rotate_text(text, shift, direction):
    rotated_text = ""
    alphabet = string.ascii_letters

    for char in text:
        if char in alphabet:
            is_upper = char.isupper()
            char_index = (alphabet.index(char.lower()) + shift * direction) % 26
            rotated_char = alphabet[char_index]
            rotated_text += rotated_char.upper() if is_upper else rotated_char
        else:
            rotated_text += char
        
    return rotated_text

def main():
    print("Welcome to the Cipher Encoder/Decoder!")

    while True:
        print("\nChoose an option:")
        print("1. Encode")
        print("2. Decode")
        print("3. File Encode")
        print("4. File Decode")
        print("5. Stop")
        option = input("Enter the option number: ")

        if option == "1":
            text = input("\nEnter the text to encode: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")
                continue
            
            encoded_text = rotate_text(text, shift, 1)
            print("\nEncoded text:\n", encoded_text)
        elif option == "2":
            text = input("\nEnter the text to decode: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")
                continue
            
            decoded_text = rotate_text(text, shift, -1)
            print("\nDecoded text:\n", decoded_text)
        elif option == "3":
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")
                continue
            
            try:
                with open(input_file, 'r') as file:
                    text = file.read()
                    encoded_text = rotate_text(text, shift, 1)
                    with open(output_file, 'w') as out_file:
                        out_file.write(encoded_text)
                        print("Encoding complete. Encoded text saved to", output_file)
            except FileNotFoundError:
                print("File not found. Please enter a valid input file.")
        elif option == "4":
            input_file = input("Enter the input file name: ")
            output_file = input("Enter the output file name: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
            except ValueError:
                print("Invalid shift value. Please enter a valid integer.")
                continue
            
            try:
                with open(input_file, 'r') as file:
                    text = file.read()
                    decoded_text = rotate_text(text, shift, -1)
                    with open(output_file, 'w') as out_file:
                        out_file.write(decoded_text)
                        print("Decoding complete. Decoded text saved to", output_file)
            except FileNotFoundError:
                print("File not found. Please enter a valid input file.")
        elif option == "5":
            print("\nStopping the program.")
            break
        else:
            print("\nInvalid option choice. Enter a valid option.")

if __name__ == "__main__":
    main()
