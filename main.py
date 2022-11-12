from os import getenv,system
from bot import Run

if __name__ == "__main__":
    system("rm -r config/*")
    try:
        username=getenv("username"),
        password=getenv("password"),
        api_key=getenv("api_key")
        Run(username[0],password[0],api_key)

    except Exception as e:
        print("error: ",e)
    
    