from .__wikipedia__ import Wikipedia

class Analysis():
    def __init__(self) -> None:
        print("ok")
  
    def __algo__(self)->list:
        return ['']

    def __analysis__(self,url:str,q:str,_type:str)->tuple[str,str,list]:
        _type:str = _type
        content:str = Wikipedia(q)
        hashtags:list[str] =['ss']

        return _type,content,hashtags