from requests import get
from random import randint

class Media():
    def __init__(
        self,api_key:str
        ) -> None:
        self.url:str = "https://pixabay.com/api/"
        self.api_key=api_key
        self.colors =[
            "grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue", "lilac", "pink", "white", "gray", "black", "brown"
        ]

    def image(self,q:str,orientation:str="vertical",category:str="all",_type:str="all")->tuple[list,str]:
        data:list=[]

        res = get(
            url=self.url,
            params={
                "key":self.api_key,
                "lang":"en",
                "safesearch":"true",
                "orientation":orientation,
                "q":q,
                "category":category,
                "image_type":_type,
                "colors":self.colors[randint(0,len(self.colors))],
                "min_width":1080,
                "min_height":1080,
                "per_page":5
            }
        )
        for x in res.json()['hits']:
            data.append(x['webformatURL'])

        return data,q

    def video(self,q:str,category:str="all",_type:str="all")->tuple[list,str]:
        data:list=[]

        res = get(
            url=self.url+"/videos",
            params={
                "key":self.api_key,
                "lang":"en",
                "safesearch":"true",
                "q":q,
                "category":category,
                "video_type":_type,
                "min_width":1080,
                "min_height":1080,
                "per_page":3
            }
        )
        for x in res.json()['hits']:
            data.append(x['videos']['small']['url'])
    
        return data,q