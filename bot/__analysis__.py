from time import sleep

class Analysis():
    def __init__(self,text:str) -> None:
        print("hello form analysis "+text)

    def __sleeper__(self,time:int):
        """
        ### `time` is in hour(s)
        """
        sleep(time*60*60)

    def __uploader__(self):
        pass