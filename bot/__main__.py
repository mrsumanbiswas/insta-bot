from time import sleep
from .__insta__ import Bot
from .__media__  import Media
from .__analysis__ import Analysis

class Run(Bot,Media,Analysis):
    def __init__(self,username:str,password:str,api_key:str,**kwargs) -> None:
        super().__init__(username,password)
        super(Bot,self).__init__(api_key)
        super(Media,self).__init__()
        self.__run__()

    def __uploader__(self,_type:str,url:str,content:str,hashtags:list[str]):
        pass

    def __sleeper__(self,time:int):
        """
        ### `time` is in hour(s)
        """
        print(f"I'm going to sleep for next {time} hour(s).")
        sleep(time*60*60)
        print("My sleep is done!")

    def __run__(self):
        while True:
            data = super().__algo__()
            if data['type'] == "image":
                content=super().image(
                    q=data['query'],
                    orientation='any',
                    category=data['category']
                )
            elif data["type"] == "video":
                content=super().video(
                    q=data['query'],
                    category=['category'],
                )
            elif data["type"] == "story":
                content=super().image(
                    q=data['query'],
                    category=data['category']
                )
            else:
                content = ([],"")

            for post in content[0]:
                result = super().__analysis__(post,content[1],data['type'])
                self.__uploader__(result[0],result[1],result[2],result[3])
            self.__sleeper__(0.001)
