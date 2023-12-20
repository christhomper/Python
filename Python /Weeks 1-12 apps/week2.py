#Created: Thursday Jan 26 10:30:16 2023
#author: christhompson

user_text = input('Enter text:') #Ex. Listen, Mr. Thompson, calm down.
output = 0  #set variable

for char in user_text:  
    if not(char in " .,"): #excludes spaces, periods, and commas from character count
        output += 1 
print(output) #prints character count output excluding spaces, periods, and commas
