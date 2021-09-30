import string

#Jungle language is a language, known predominantly in the South-Eastern part of Nigeria. 
#One may think of it as a way of encrypting messages written in English language.
#The language is simple: for every consonant in a sentence, the latter 'a' is added.
#All vowels are replaced with numbers from 1-5 i.e., a:1, b;2, c:3, d:4, e:5
#For example, the sentence, I like food, will be written in jungle language as: 3 la3ka2 f44da
#Note: All punctuations are not changed


def translate(text):
    """
    Takes in one input: text
    Assumes text as str,
    Returns the jungle_language word, phrase or sentence of text

    """

    alphabets=string.ascii_lowercase+string.ascii_uppercase
    vowels={'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5', 'A':'1', 'E':'2', 'I':'3', 'O':'4', 'U':'5'}
    consonants=[]
    for letter in alphabets:
        if letter not in vowels.keys():
            consonants.append(letter)

    output_list=[]
    for i in range(len(text)):
        if text[i] in consonants:
            output_list.append(text[i]+'a')
        elif text[i] in vowels:
            output_list.append(vowels[text[i]])   
        else:
            output_list.append(text[i])
    return ''.join(output_list)


#Example
a='Hi!'
print(translate(a))

a='I love playing with my dog'
print(translate(a))

a='The excitement that flushed through my veins when I was told I will be attending a foreign university was out of bounds. Every night, all I could do was watch the stars by my window, ponder on how fast I could reach my university in a matter of minutes. Thus, it was not what I had dreamed. All the conflicts that I had to face during the journey were enough to make the journey tiring.'
print('\n'+translate(a))

a='The three-star hotel had the best life can offer. It had nice delicacies in the food menu, nice bathtub, a large bed that could fit four of me, a chandelier that glittered, Full-length mirror with lighting, and free Wi-Fi.  It was a memorable twenty-four hours.'
print('\n'+translate(a))

