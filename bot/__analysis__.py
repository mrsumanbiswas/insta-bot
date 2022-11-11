from .__media__  import Media

class Analysis(Media):
    def __init__(self,api_key:str) -> None:
        super().__init__(api_key)

  
    def __analysis__(self):
        print('s')
        pass