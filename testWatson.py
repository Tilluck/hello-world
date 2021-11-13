''' Functuon to use watson APIs to translate English text to French'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ['url']

#added the IBM code to access their APIs#
'''setting the paramitemers for watson api'''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator,
)
language_translator.set_service_url(url)

#function to convert English text to French
def english_to_french(english_text):
    '''sending a get request to  to watson'''
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

#function to convert French text to English
def french_to_english(french_text):
    '''sending a get request to  to watson'''
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
    


import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_EnglishToFrench(self):
        if EnglishToFrench is not None:
            self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_FrenchToEnglish(self):
        if FrenchToEnglish is not None:
            self.assertEqual(frenchToEnglish('Bonjour'),'Hello')


if __name__ == '__main__':
    unittest.main()
