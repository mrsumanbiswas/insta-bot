from time import sleep,time
from os import system
from requests import get
from .__insta__ import Bot
from .__media__  import Media
from .__analysis__ import Analysis

class Run(Bot,Media,Analysis):
    def __init__(self,username:str,password:str,api_key:str) -> None:
        super().__init__(username,password)
        super(Bot,self).__init__(api_key)
        super(Media,self).__init__()
        self.__run__()

    def __uploader__(self,_type:str,url:str,content:str,hashtags:list[str]):
        if _type == "video":
            name=str(time())+".mp4"
        else:
            name=str(time())+".jpg"

        for i in hashtags:
            content += f"\n#{i}"

        open("temp/"+name,"wb").write(get(url).content)
        if _type == "image":
            super().upload_image("temp/"+name,caption=content)
        elif _type == "video":
            super().upload_video("temp/"+name,caption=content)
        else:
            super().upload_story("temp/"+name)

        system(f"rm -r temp/{name}")

    def __sleeper__(self,time:int):
        """
        ### `time` is in hour(s)
        """
        print(f"I'm going to sleep for next {time} hour(s).")
        system("rm -r temp/*")
        self.query.reverse()
        sleep(time*60*60)
        print("My sleep is done!")

    def __run__(self):
        query_index=0
        category_index = 0
        while True:
            data = super().__algo__(category_index,query_index)

            if category_index == len(self.category):
                category_index =0
            else:
                category_index += 1
        
            if query_index == len(self.query):
                query_index =0
            else:
                query_index += 1
            
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
                    category=data['category'],
                    _type="animation"
                )
            else:
                content = ([],"")

            for post in content[0]:
                result = super().__analysis__(post,content[1],data['type'])
                self.__uploader__(result[0],result[1],result[2],result[3])
            
            self.__sleeper__(0.001)


