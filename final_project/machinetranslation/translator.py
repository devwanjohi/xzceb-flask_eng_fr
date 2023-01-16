"""
translator file that uses ibm watson api to translate different languages
"""
import json
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
language_translator = LanguageTranslatorV3(
    version = '2018-05-01', 
    authenticator=authenticator
    )
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)
# Translating to French
def english_to_french( english_text ):
    """
    Function to translate english to french
    """
    french_text = language_translator.translate(
        text = english_text, 
        model_id = 'en-fr'
        ).get_result()
    return french_text.get("translations")[0].get("translation")

# Translating to English
def french_to_english( french_text ):
    """
    Function to translate french to english
    """
    english_text = language_translator.translate(
        text = french_text, 
        model_id = 'fr-en'
        ).get_result()
    return english_text.get("translations")[0].get("translation")