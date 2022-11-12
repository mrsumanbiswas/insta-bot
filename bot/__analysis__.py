from datetime import datetime
from .__wikipedia__ import Wikipedia

class Analysis():
    def __init__(self) -> None:
        print("I'm ready boss!")
        self.category =[
            "backgrounds", "nature", "science", "education", "feelings", "health", "people", "religion", "places", "animals", "industry", "computer", "food", "sports", "transportation", "travel", "buildings", "business", "music"
        ]
        self.query = []
  
    def __algo__(self)->dict:
        hour= datetime.now().hour
        category_index = 0
        query_index=0
        _type = "image"

        if hour >= 0 and hour < 4:
            _type = "story"
        elif hour >= 4 and hour <8:
            _type = "video"
        elif hour >= 8 and hour <12:
            _type = "image"
        elif hour >= 12 and hour <16:
            _type = "story"
        elif hour >= 16 and hour <20:
            _type = "video"
        else:
            pass
        
        if category_index == len(self.category):
            category_index =0
        else:
            category_index += 1
        
        if queary_index == len(self.query):
            queary_index =0
        else:
            queary_index += 1
        
        return {
            "type":_type,
            "category": self.category[category_index],
            "query":self.query[query_index]
        }

    def __analysis__(self,url:str,q:str,_type:str)->tuple[str,str,list]:
        content:str = Wikipedia(q)
        hashtags:list[str] =['dizzytechnician']

        hashtags.append(q.split(" "))
        content_tag = content.split(" ")
        for i in range(5):
            hashtags.append(content_tag[i])
    
        return _type,url,content,hashtags