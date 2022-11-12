from os import getenv
from bot import Run

if __name__ == "__main__":
    try:
        username=getenv("username"),
        password=getenv("password"),
        api_key=getenv("api_key")

    except Exception as e:
        print("error: ",e)
    
    Run(username[0],password[0],api_key)
    