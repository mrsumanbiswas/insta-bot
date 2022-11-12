from datetime import datetime
from .__wikipedia__ import Wikipedia

class Analysis():
    def __init__(self) -> None:
        print("I'm ready boss!")
        self.category =[
            "backgrounds", "nature", "science", "education", "feelings", "health", "people", "religion", "places", "animals", "industry", "computer", "food", "sports", "transportation", "travel", "buildings", "business", "music"
        ]
  
    def __algo__(self)->dict:
        hour= datetime.now().hour
        index = 0

        if hour >= 0 and hour < 4:
            pass
        elif hour >= 4 and hour <8:
            pass
        elif hour >= 8 and hour <12:
            pass
        elif hour >= 12 and hour <16:
            pass
        elif hour >= 16 and hour <20:
            pass
        else:
            pass
        
        if index == len(self.category):
            index =0
        else:
            index += 1
        
        return {
            "type":"all",
            "category": self.category[index]
        }

    def __analysis__(self,url:str,q:str,_type:str)->tuple[str,str,list]:
        content:str = Wikipedia(q)
        hashtags:list[str] =['dizzytechnician']

        hashtags.append(q.split(" "))
        content_tag = content.split(" ")
        for i in range(5):
            hashtags.append(content_tag[i])
    
        return _type,url,content,hashtags