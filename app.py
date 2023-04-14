from flask import Flask,render_template,request
from googletrans import Translator
import sys
import re

app = Flask(__name__)

def get_output(english_text):
    # Initialize translator object
    translator = Translator()

    # English text to translate
    # Translate to Telugu
    telugu_text = translator.translate(english_text, dest='te').text

    # Print the Telugu translation
    print("Telugu translation:", telugu_text)

    # Define a dictionary of Telugu letters and their corresponding English phonetic transcriptions
    telugu_to_english = {
        'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ee', 'ఉ': 'u', 'ఊ': 'oo', 'ఋ': 'ri',
        'ౠ': 'rri', 'ఎ': 'e', 'ఏ': 'ee', 'ఐ': 'ai', 'ఒ': 'o', 'ఓ': 'oo', 'ఔ': 'au',
        'క': 'k', 'గ': 'g', 'చ': 'ch', 'ట': 'ta', 'డ': 'd', 'త': 't', 'ద': 'd',
        'న': 'n', 'ప': 'p', 'బ': 'b', 'మ': 'm', 'య': 'y', 'ర': 'r', 'ల': 'l',
        'వ': 'v', 'శ': 'sh', 'ష': 'sha', 'స': 's', 'హ': 'h',
        'ా': 'aa', 'ి': 'i', 'ీ': 'ee', 'ు': 'u', 'ూ': 'oo','ృ': 'ri',
    'ౄ': 'rii',
    'ెె': 'e',
    'ేే': 'ee',
    'ైై': 'ai',
    'ొొ': 'o',
    'ోో': 'oo',
    'ౌ': 'au','ం':'an', 'ః':'aha' ,'౦': '0', '౧': '1',
        '౨': '2', '౩': '3', '౪': '4', '౫': '5', '౬': '6', '౭': '7', '౮': '8',
        '౯': '9', 
    }

    # Split the Telugu text into words
    words = telugu_text.split()

    # Split each word into individual letters
    letters = []
    for word in words:
        word_letters = [letter for letter in word]
        letters.append(word_letters)

    # Create an empty list to store matching letters
    matches = []

    # Loop through each letter in the letters list and compare with the keys in the telugu_to_english dictionary
    for word_letters in letters:
        for letter in word_letters:
            if letter in telugu_to_english:
                # If it is, append the corresponding English phonetic transcription to the matches list
                matches.append(telugu_to_english[letter])

    # Convert the matches list to a string
    matches_str = ''.join(matches)

    # Print the matching letters and their corresponding English phonetic transcriptions
    print('Matching letters:', matches_str)
    return matches_str

@app.route('/' , methods = ['POST','GET'])
def hello():
    if request.method == 'POST':
        print(request.form.get('text'))
        return get_output(request.form.get('text'))
    else:
        return render_template("home.html")

if __name__ == '__main__':
   app.run()