import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['api_key']
api_url = os.environ['api_url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(api_url)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(text="Hello World", model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(text="Bonjour le monde", model_id='fr-en').get_result()
    return englishText