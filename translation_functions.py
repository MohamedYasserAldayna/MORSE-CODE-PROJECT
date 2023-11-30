# Both dictionaries are imported at the start
import morsetotext
import texttomorse 


# The function for the translation of text to morse is defined, it uses the user input as parameter
def trans_text_to_morse (input_t):
    # A new empty string variable output_m is created, the translation will be added to this variable,
    output_m = " "
    # A for loop that iterates for each letter in the user's input
    for letter in input_t:
        # An if condition to check whether the letter is a space or not
        
        if letter != " " :
            
            #If the letter is not a space, the variable letter_translation is initialized
            
            letter_translation = texttomorse.text_to_morse[letter.upper()]

            #The variable is assigned to the code correlatng to the letter in accordance with the text_to_morse dictionary
            
            output_m += letter_translation + " "

            #The value of letter_translation is implemented into output_m aswell as a space after it 

        else:
            
            #If the letter is space, a space is added to output_m 

            output_m += " "
    
    
    # The function returns output_m (the morse translation)
    
    return output_m

# The function for the translation of morse to text is defined, it uses the user input as parameter

def trans_morse_to_text (input_m):
    
    # The variable spl_input is created and is assigned to input_m after it has been run through the split function 
    # The seperator of the split function is set to a space character

    spl_input = input_m.split(" ")

    # A new empty string variable output_t is created, the translation will be added to this variable,

    output_t = ""

    # A for loop that iterates for each word in the variable spl_input

    for word in spl_input:

        # An if condition to check whether the word is a slash or not


        if word != "/":

            #If the word is not a slash, the variable symbol_sequence is initialized

            symbol_sequence = morsetotext.morse_to_text[word]

            #The variable is assigned to the letter correlatng to the code sequence in accordance with the morse_to_text dictionary

            output_t += symbol_sequence

            #The value of symbol_sequence is implemented into output_t 

        else:

            #If the word is slash, a space is added to output_t

            output_t += " "
    # The function returns output_t (the text translation)
    return output_t
    



