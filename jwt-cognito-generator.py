import base64
import hashlib
import hmac
import string
import boto3

cognito_client = boto3.client('cognito-idp')


client_id = "to_configure"
client_secret = "to_configure"
userpool_id = "to_configure"

username = "to_configure"
password =  "to_configure"


def sign_in( username: string, password: string):
    response = cognito_client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        ClientId= client_id,
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password,
            # 'SECRET_HASH': get_secret_hash(username, client_id, client_secret), 
        }
    )

    http_status_code = int(response['ResponseMetadata']['HTTPStatusCode'])

    if http_status_code == 200:
        print(f"Access token: {response['AuthenticationResult']['AccessToken']}")
        print(f"\nId token: {response['AuthenticationResult']['IdToken']}")
    else:
        print('Unauthorized')

   
    
def get_acces_key(username, password):
    return sign_in(username, password).get('AuthenticationResult').get('IdToken')

def get_secret_hash(username, client_id, client_secret):
    message = bytes(username+client_id,'utf-8')
    client_secret = bytes(client_secret,'utf-8')
    secret_hash = base64.b64encode(hmac.new(client_secret, message, digestmod=hashlib.sha256).digest()).decode()

    return secret_hash


sign_in(username, password)