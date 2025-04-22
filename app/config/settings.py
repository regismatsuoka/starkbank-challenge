import os

STARKBANK_PROJECT_ENV = os.getenv('STARKBANK_PROJECT_ENV')
STARKBANK_PROJECT_ID = os.getenv('STARKBANK_PROJECT_ID')
STARKBANK_PRIVATE_KEY_CONTENT =os.getenv('STARKBANK_PRIVATE_KEY_CONTENT')

def get_credentials():
    if STARKBANK_PRIVATE_KEY_CONTENT is None:
            raise EnvironmentError("Faltam informações no arquivo de credenciais.")
    return  {"environment" : STARKBANK_PROJECT_ENV, 
             "id" : STARKBANK_PROJECT_ID,
             "key" : STARKBANK_PRIVATE_KEY_CONTENT}