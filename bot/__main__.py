from time import sleep
from .__insta__ import Bot
from .__analysis__ import Analysis

class Run(Bot,Analysis):
    def __init__(self,username:str,password:str,api_key:str,**kwargs) -> None:
        super().__init__(username,password)
        super(Bot,self).__init__(api_key)
        self.__run__()

    def __sleeper__(self,time:int):
        """
        ### `time` is in hour(s)
        """
        print(f"I'm going to sleep for next {time} hour(s).")
        sleep(time*60*60)
        print("My sleep is done!")

    def __run__(self):
        while True:
            super().__analysis__()
            self.__sleeper__(0.001)
