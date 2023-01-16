""" translator file that uses ibm watson api to translate different languages """
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authenticator
authenticator = IAMAuthenticator( apikey )
# setup service
lt = LanguageTranslatorV3(version = '2018-05-01', authenticator=authenticator)
lt.set_service_url(url)
# Translating to French
def english_to_french( english_text ):
    #write the code here
    """Function to translate english to french"""
    french_text = lt.translate(text = english_text, model_id = 'en-fr').get_result()
    return french_text
def french_to_english( french_text ):
    #write the code here
    """Function to translate french to english"""
    english_text = lt.translate(text = french_text, model_id = 'fr-en').get_result()
    return english_text
english_to_french('Hello World')
french_to_english('Bonjour le monde')
