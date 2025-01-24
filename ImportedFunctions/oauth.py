import os
from dotenv import load_dotenv
import secrets
import webbrowser

load_dotenv("./.env")

state = None

def oAuthGet():
    global state
    state = secrets.token_urlsafe(10)

    endpoint = os.getenv("OAUTHENDPOINT") + f"?client_id={os.getenv("CLIENTID")}&redirect_uri={os.getenv("REDIRECTURI")}&state={state}"
    webbrowser.open(endpoint)
    #print(state)
    #return state
    