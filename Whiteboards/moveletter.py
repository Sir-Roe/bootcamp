import re
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') -> igPay atinlay siay oolcay
# pig_it('Hello world !')    -> elloHay orldway !
def moveletter(str1:str):
    return " ".join([word[1:]+ word[0] + 'ay' if word.isalpha() else word for word in str1.split()])

print(moveletter('pig latin is cool'))