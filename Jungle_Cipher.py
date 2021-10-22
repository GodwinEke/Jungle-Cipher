import string

#Jungle language is a language, known predominantly in the South-Eastern part of Nigeria. 
#One may think of it as a way of encrypting messages written in English language.
#The language is simple: for every consonant in a sentence, the latter 'a' is added.
#All vowels are replaced with numbers from 1-5 i.e., a:1, b;2, c:3, d:4, e:5
#For example, the sentence, I like food, will be written in jungle language as: 3 la3ka2 f44da
#Note: All punctuations are not changed


class translate():
    """
    Takes in one input: text
    Assumes text as str,
    Returns the jungle_language word, phrase or sentence of text

    """
    def __init__(self,text):
        self.text=text

    def encrypt(self):
        alphabets=string.ascii_lowercase+string.ascii_uppercase
        vowels={'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5', 'A':'1', 'E':'2', 'I':'3', 'O':'4', 'U':'5'}
        consonants=[]
        for letter in alphabets:
            if letter not in vowels.keys():
                consonants.append(letter)

        output_list=[]
        for i in range(len(self.text)):
            if self.text[i] in consonants:
                output_list.append(self.text[i]+'a')
            elif self.text[i] in vowels:
                output_list.append(vowels[self.text[i]]) 
            else:
                output_list.append(self.text[i])
        return ''.join(output_list)

    def decrypt(self):
        
        self.text=''.join(reversed(list(self.text)))
        output=[]
        upper_vowels={ '1':'A', '2':'E', '3':'I', '4':'O', '5':'U'}
        lower_vowels={ '1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
        for i in range(len(self.text)):
            if self.text[i]=='a':
                continue
            elif self.text[i] in upper_vowels.keys() and self.text[i-1] in string.ascii_uppercase :
                output.append(upper_vowels[self.text[i]])
            elif self.text[i] in lower_vowels.keys() and self.text[i-1] in string.ascii_lowercase :
                output.append(lower_vowels[self.text[i]])
            else:
                output.append(self.text[i])
        return ''.join(reversed(output))
    
#Example
#a=translate('I would like to get the latest Iphone pro 13!!').encrypt()
#print(a)

#a=translate('\nTaha2 2xaca3ta2ma2nata taha1ta fala5saha2da tahara45gaha maya va23nasa waha2na 3 wa1sa ta4lada 3 wa3lala ba2 1tata2nada3naga 1 fa4ra23gana 5na3va2rasa3taya wa1sa 45ta 4fa ba45nadasa. 2va2raya na3gahata, 1lala 3 ca45lada da4 wa1sa wa1tacaha taha2 sata1rasa baya maya wa3nada4wa, pa4nada2ra 4na ha4wa fa1sata 3 ca45lada ra21caha maya 5na3va2rasa3taya 3na 1 ma1tata2ra 4fa ma3na5ta2sa. 1la1sa, 3ta  wa1sa na4ta waha1ta 3 ha1da dara21ma2da. 1lala taha2 ca4nafala3catasa taha1ta 3 ha1da ta4 fa1ca2 da5ra3naga taha2 ja45rana2ya wa2ra2 2na45gaha ta4 ma1ka2 taha2 ja45rana2ya ta3ra3naga. Taha2 tahara22-sata1ra ha4ta2la ha1da taha2 ba2sata la3fa2 ca1na 4fafa2ra. 3ta ha1da na3ca2 da2la3ca1ca32sa 3na taha2 fa44da ma2na5, na3ca2 ba1tahata5ba, 1 la1raga2 ba2da taha1ta ca45lada fa3ta fa45ra 4fa ma2, 1 caha1nada2la32ra taha1ta gala3tata2ra2da, Fa5lala-la2nagataha ma3rara4ra wa3taha la3gahata3naga, 1nada fara22 Wa3-Fa3.  3ta wa1sa 1 ma2ma4ra1bala2 tawa2nataya-fa45ra ha45rasa.')
#print(a.decrypt().lower())







