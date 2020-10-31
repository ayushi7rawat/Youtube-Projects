'''
Build a Translator in Python
Author: Ayushi Rawat
'''

#import the package
from googletrans import Translator

# Store some text for translation in french language
text = '''  Pour souvent, quand sur mon canapé je mens
D'humeur vacante ou songeuse,
Ils clignotent sur cet œil intérieur
Quel est le bonheur de la solitude;
Et puis mon cœur se remplit de plaisir,
Et danse avec les jonquilles. '''

# Create an instance of Translator to use
translator = Translator()

# detect the language
lang = translator.detect(text)
print(lang)
print(' ')

# Call the translate()
translated = translator.translate(text, dest = 'en')

#print the result
print(translated.text)
