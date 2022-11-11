from .__wikipedia__ import Wikipedia

class Analysis():
    def __init__(self) -> None:
        print("ok")
  
    def __algo__(self)->list:
        return ['']

    def __analysis__(self,url:str,q:str,_type:str)->tuple[str,str,list]:
        content:str = Wikipedia(q)
        hashtags:list[str] =['auto_insta']

        hashtags.append(q.split(" "))
        content_tag = content.split(" ")
        for i in range(5):
            hashtags.append(content_tag[i])
    
        return _type,url,content,hashtags