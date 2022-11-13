from datetime import datetime
from random import randint
from .__wikipedia__ import Wikipedia

class Analysis():
    def __init__(self) -> None:
        print("I'm ready boss!")
        self.category =[
            "backgrounds", "nature", "science", "education", "feelings", "health", "people", "religion", "places", "animals", "industry", "computer", "food", "sports", "transportation", "travel", "buildings", "business", "music"
        ]
        self.query = [ 'google', 'youtube', 'instagram', 'facebook', 'meta', 'india', 'germany', 'canada', 'australia', 'japan','cpp', 'golang', 'china', 'united states', 'italy', 'brazil', 'afrika', 'mountains', 'river', 'sky', 'space', 'wall', 'door', 'book', 'physics', 'computers', 'servers', 'data base', 'python', 'coding', 'bot', 'robort', 'milkyway', 'nature', 'beautiful places', 'blue', 'red', 'yello', 'green', 'black', 'gray', 'canyon', 'imac', 'macbook', 'iphone', 'samsung', 'catfish', 'salmon', 'shark', 'german shepherd', 'bulldog', 'golden retriever', 'french bulldog', 'afghan hound', 'parrots', 'sparrow', 'duck', 'pigeon', 'goat', 'camel', 'cow', 'tiger', 'wolf', 'lion', 'crab', 'cobra', 'monkey', 'rat', 'deer', 'yak', 'lamb', 'zebra', 'whale', 'eagle', 'dove', 'claw', 'wing', 'potato', 'lemon', 'tomato', 'green jack', 'pumpkin', 'paddy', 'rice', 'wheat', 'flour', 'olive', 'banana', 'guava', 'cocoanut', 'palm', 'grape', 'mango', 'berry', 'almond', 'walnut', 'jasmine', 'lily', 'jam', 'cake', 'coffee', 'tea', 'biscuit', 'arch', 'window', 'snack', 'icecream', 'soda water', 'sugar candy', 'mirror', 'roller', 'school', 'college', 'university', 'black board', 'bell', 'blobe', 'duster', 'chalk', 'principal', 'arts', 'science', 'commerce', 'fine arts', 'engineering', 'medical science', 'management', 'agriculture', 'law', 'technology', 'horticulture', 'leaf', 'log']
        self._type =['image','video','story']

    def __algo__(self)->dict:
        
        return {
            "type":self._type[randint(0,len(self._type))],
            "category": self.category[randint(0,len(self.category))],
            "query":self.query[randint(0,len(self.query))]
        }

    def __analysis__(self,url:str,q:str,_type:str)->tuple[str,str,list]:
        content:str = Wikipedia(q)
        hashtags:list[str] =['dizzytechnician']
        content_tag = content.split(" ")
        try:
            for i in range(5):
                hashtags.append(content_tag[i])
        except:
            pass
        return _type,url,content,hashtags