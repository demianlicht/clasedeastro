# -*- coding: utf-8 -*-
"""
Morse Code translator
Por: Demian Licht
Carne 171105
Astrofisica Computacional
Universidad del Valle de Guatemala

Date: 9/01/2017
"""
CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

sentence = input("Ingresar oración: ")
encodedSentence = convertToMorseCode(sentence)
print("Simbólicamente")
print(encodedSentence)

def encodeToWords(sentence):
    encodedSentence = convertToMorseCode(sentence)
    for character in encodedSentence:
        if character == '-':
            print("Dash")
        elif character == '.':
            print("Dot")
        elif character == ' ':
            print('.')
        elif character == '_':
            print("Space")

sentence = input("Ingrear oración:")
print("En palabras:")
encodeToWords(sentence)

