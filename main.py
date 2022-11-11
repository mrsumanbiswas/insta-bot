# from instabot import 
from bot import Run
from os import getenv

if __name__ == "__main__":
    try:
        username=getenv("username"),
        password=getenv("password"),
        api_key=getenv("api_key")

    except:
        username="test_user_name",
        password="test_password",
        api_key="test_api_key"

    Run(username,password,api_key)