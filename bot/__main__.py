from .__insta__ import Bot
from .__media__ import Media
from .__analysis__ import *

class Run(Bot,Media):
    def __init__(self,username:str,password:str) -> None:
        super().__init__(username,password)
