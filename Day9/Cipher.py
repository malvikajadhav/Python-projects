alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    '''
    Parameters:
        text(str): word input
        shift(int): ceaser shift
    Returns:
        Print statement
    '''
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    output = ''
    for letter in text:
        current = alphabet.index(letter)
        shifted = current + shift
        if shifted<len(alphabet)-1:
            output += alphabet[shifted]  
        else:
            new_shift = shifted%(len(alphabet)-1)
            output += alphabet[new_shift-1]           
    print(f"The encoded text is {output}")
    
def decrypt(text, shift):
    '''
    Parameters:
        text(str): word input
        shift(int): ceaser shift
    Returns:
        Print statement
    '''
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    output = ''
    for letter in text:
        current = alphabet.index(letter)
        shifted = current - shift
        if shifted>=0:
            output += alphabet[shifted]  
        else:
            new_shift = shifted+(len(alphabet)-1)
            output += alphabet[new_shift+1]           
    print(f"The encoded text is {output}")
    

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Invalid option choice")