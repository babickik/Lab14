
from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text


def sortowanie_babelkowe(lista):
    n = len(lista)
    
    if n == 0:
        return 'Pusta lista'

    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1
        if zamien == False: break
        
    return lista