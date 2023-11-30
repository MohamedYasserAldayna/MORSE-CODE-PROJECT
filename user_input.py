# The dictionaries and the functions file are imported

import translation_functions
import texttomorse
import morsetotext

# The variable first_selection is an integer entered by the user to determinate the function to use

first_selection = int(input("Please enter \"1\" to translate morse code to text, enter \"2\" to translate text to morse code\n or \"3\" for quick morse signals\n"))

# If the first condition is 1

if first_selection==1:
    
    # The variable second_selection is assigned to the morse code that the user wants to translate

    second_selection = str(input("Please enter the morse code you want to translate(leave a space between each letter and \"/\" between each word)\n"))
    
    # The variable result is assigned to the second selection after it has been run through the trans_morse_to_text

    result = translation_functions.trans_morse_to_text(second_selection)

    # The result is printed

    print(result)

# If the first condition is 2

elif first_selection==2:

    # The variable second_selection is assigned to the text that the user wants to translate

    second_selection = str(input("Please enter the text you want to translate\n")) 

    # The variable result is assigned to the second selection after it has been run through the trans_yext_to_morse

    result = translation_functions.trans_text_to_morse(second_selection)

    # The result is printed

    print(result)   

# If the first_selection is 3

elif first_selection == 3:
    
    # The second_selection is assigned to the integer entered by the user

    second_selection=int(input("Enter \"1\" for SOS\nEnter \"2\" for GA\nEnter \"3\" for AAA\nEnter \"4\" for QTH\nEnter \"5\" for ACK\nEnter \"6\" for RPT\nEnter \"7\" for ROGER\n"))

    #  If second_selection is 1 

    if second_selection == 1:

        # The variable result is assigned to the string "SOS" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("SOS")

        # The result is printed

        print(result)

    #  If second_selection is 2

    elif second_selection == 2:

        # The variable result is assigned to the string "GA" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("GA")

        print(result)

    #  If second_selection is 3

    elif second_selection == 3:

        # The variable result is assigned to the string "AAA" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("AAA")

     # The result is printed

        print(result)

    #  If second_selection is 4

    elif second_selection == 4:

        # The variable result is assigned to the string "QTH" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("QTH")

    # The result is printed

        print(result)

    #  If second_selection is 5

    elif second_selection == 5:

        # The variable result is assigned to the string "ACK" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("ACK")

    # The result is printed

        print(result)

    #  If second_selection is 6

    elif second_selection == 6:

        # The variable result is assigned to the string "RPT" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("RPT")

     # The result is printed

        print(result)

    #  If second_selection is 7

    elif second_selection == 7:

        # The variable result is assigned to the string "ROGER" after it has been run through the trans_yext_to_morse

        result = translation_functions.trans_text_to_morse("ROGER")

     # The result is printed

        print(result)

    else:
        
        # If the user enters a number that is not from 1 to 7
         
        print("Please enter a valid command!")

else:

    # If the user enters a number that is not from 1 to 3

    print("Please enter a valid command!")
    