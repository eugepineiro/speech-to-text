import string, re

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

def remove_accents(text):
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u")

    return text

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    text = re.sub(pattern, '', text)

    return text

def remove_all(text):
    text = remove_punctuation(text)
    text = text.lower()
    text = remove_accents(text)
    text = remove_special_characters(text)

    return text


text = remove_punctuation("Hola, ¿qué tal?")
text = text.lower()
text = remove_accents(text)
text = remove_special_characters(text)
print(text)