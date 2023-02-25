# coding=utf-8
import configparser
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# Load the API key from a configuration file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config.get('ibm', 'api_key')

# Create an authenticator object with the API key
authenticator = IAMAuthenticator(api_key)

# Create a LanguageTranslatorV3 object with the authenticator and service URL
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/dc74c055-0741-44f4-9ca4-8fde68fc5703')

# Translate a text using the Language Translator service
translation = language_translator.translate(
    text='Hello', model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

# List identifiable languages
# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))

# # Identify
# language = language_translator.identify(
#     'Language translator translates text from one language to another').get_result()
# print(json.dumps(language, indent=2))

# # List models
# models = language_translator.list_models(
#     source='en').get_result()
# print(json.dumps(models, indent=2))

# # Create model
# with open('glossary.tmx', 'rb') as glossary:
#     response = language_translator.create_model(
#         base_model_id='en-es',
#         name='custom-english-to-spanish',
#         forced_glossary=glossary).get_result()
#     print(json.dumps(response, indent=2))

# # Delete model
# response = language_translator.delete_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(response, indent=2))

# # Get model details
# model = language_translator.get_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(model, indent=2))

#### Document Translation ####
# List Documents
result = language_translator.list_documents().get_result()
print(json.dumps(result, indent=2))

# Translate Document
with open('en.pdf', 'rb') as file:
    result = language_translator.translate_document(
        file=file,
        file_content_type='application/pdf',
        filename='en.pdf',
        model_id='en-fr').get_result()
    print(json.dumps(result, indent=2))

# Document Status
result = language_translator.get_document_status(
    document_id='{document id}').get_result()
print(json.dumps(result, indent=2))

# Translated Document
with open('translated.pdf', 'wb') as f:
    result = language_translator.get_translated_document(
        document_id='{document id}',
        accept='application/pdf').get_result()
    f.write(result.content)

# Delete Document
language_translator.delete_document(document_id='{document id}')
