import re
import nltk
from nltk.corpus import words, names

nltk.download('words', quiet = True)
nltk.download('names', quiet = True)

word_list = words.words()
name_list = names.words()

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, shift):

    words = text.split()

    decrypted_msg = []

    for word in words:

        decrypted_word = ''

        for char in word:
          
            if char.lower() in letters:
                shift_value = ( letters.index(char) + shift ) % 26

                decrypted_word += letters[shift_value]

            else:
                decrypted_word += char

        decrypted_msg.append(decrypted_word) 

    result = " ".join(decrypted_msg)
        
    return result


def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)


def crack(cipher_text):

    for i in range(0, 26):

        text = decrypt(cipher_text, i)

        possible_words = text.split()

        word_count = 0

        for possible_word in possible_words:

            word = re.sub(r'[^A-Za-z]+', '', possible_word)

            if word.lower() in word_list or word in name_list:

                word_count += 1


        percentage = int( word_count / len(cipher_text.split()) * 100 )
        
        if percentage > 50:
            return text 
   
