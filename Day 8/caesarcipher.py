alphabet_lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encode(textEncode, shift):
    encoded_text = ""
    for char in textEncode:
        if char in alphabet_lowercase:
            index = 0
            while index < len(alphabet_lowercase):
                if alphabet_lowercase[index] == char:
                    break
                index += 1
            # Compute new shifted index
            new_index = (index + shift) % len(alphabet_lowercase)
            encoded_text += alphabet_lowercase[new_index]
        else:
            # If the character is not in the alphabet, add it as is
            encoded_text += char
    return encoded_text

def decode(textDecode, shift):
    decoded_text = ""
    for char in textDecode:
        if char in alphabet_lowercase:
            index = 0
            while index < len(alphabet_lowercase):
                if alphabet_lowercase[index] == char:
                    break
                index += 1
            # Compute new shifted index
            new_index = (index - shift) % len(alphabet_lowercase)
            decoded_text += alphabet_lowercase[new_index]
        else:
            # If the character is not in the alphabet, add it as is
            decoded_text += char
    return decoded_text

typeOperation = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("How much would you like to shift by: "))

if typeOperation == "encode":
    encoded_message = encode(text, shift)
    print(f"Encoded message: {encoded_message}")

elif typeOperation == "decode":
    decoded_message = decode(text, shift)
    print(f"Decoded message: {decoded_message}")
