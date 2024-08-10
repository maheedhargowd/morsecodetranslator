english_to_morse = {
    # alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    # numbers 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    # special characters
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '(': '-.--.', '/': '-..-.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}
morse_to_english = { 

}
values = list(english_to_morse.keys())
keys   = list(english_to_morse.values())

for key ,value in zip(keys,values) :
    morse_to_english[key]=value

user_input = input('enter an english string :')   


def english_to_morsecode_translator(text):
    output = ''
    if len(text) == 0:
        print('given string is empty .')

    else :

        for i in text:
            
            output += english_to_morse[i.capitalize()] + '   '
        
        return output.strip()

def morse_english_translator (text):
    output=''
    words = text.split('       ')
    

    letters =[]
    for i in range(len(words)):
        letters.append(words[i].split('   ')+[' '])
    
    
    for i in letters :
        for j in i:
            output+=morse_to_english[j]
    
    return output


e_m_output=english_to_morsecode_translator(user_input)
print(e_m_output)
m_e_output = morse_english_translator (e_m_output) 
print('converting the above morse to english :',m_e_output)






