import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def ceaser(text, shift, direction):
    '''
    Parameters:
        text(str): word input
        shift(int): ceaser shift
        direction(str): encode/decode
    Returns:
        Print statement
    '''
    output = ''
    if direction == 'decode':
        shift *=-1
    for letter in text:
        if letter in alphabet:
            current = alphabet.index(letter)
            shifted = current + shift
            if shifted<len(alphabet)-1 and shifted>=0:
                output += alphabet[shifted]  
            else:
                if shifted>0:
                    new_shift = shifted%(len(alphabet)-1)
                    output += alphabet[new_shift-1]   
                else: 
                    new_shift = shifted+(len(alphabet)-1)
                    output += alphabet[new_shift+1]  
        else:
            output+=letter       
    print(f"The {direction}d text is {output}")


flag = True
while flag ==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    response = input("Do you want to continue using ceaser cipher?\nType yes or no\n")
    if response == 'no':
        print("Goodbye!")
        flag = False
