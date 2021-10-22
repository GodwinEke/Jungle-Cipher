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





