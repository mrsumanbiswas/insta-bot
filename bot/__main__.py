from time import sleep
from .__insta__ import Bot
from .__media__ import Media
from .__analysis__ import Analysis

class Run(Bot,Media,Analysis):
    def __init__(self,username:str,password:str,api_key:str,**kwargs) -> None:
        super().__init__(username,password)
        super(Bot,self).__init__(api_key)
        super(Media,self).__init__("test")

        def __sleeper__(self,time:int):
            """
            ### `time` is in hour(s)
            """
            sleep(time*60*60)

    while True:
