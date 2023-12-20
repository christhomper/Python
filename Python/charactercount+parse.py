user_text = input('Enter text to be counted:') # example: Listen, Mr. Jones, calm down
print('original string length:', len (user_text))
chars_to_remove = ' .,'
char_count = 0
for character in user_text:
    if character not in chars_to_remove:
    #if character != ' ' and character != ',' and character !: '.':
        char_count += 1
print ("parsed string Length:")
print (char_count)
