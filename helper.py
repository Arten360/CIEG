from dotenv import load_dotenv, find_dotenv 
import os

def load_env():
    _ = load_dotenv(find_dotenv())


def load_emaps_api_key(ret_key=True):
    load_env()
    global api_key
    api_key = os.getenv("R02uJ4sceYf2b")
    
    if ret_key:
        return api_key
    return