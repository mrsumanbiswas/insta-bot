import re
import wikipedia

def Wikipedia(quary: str) -> str:
    try:
        Summary = wikipedia.summary(quary, sentences=3)
        texts2 = re.sub("\[.*?\]", "", Summary)
        texts3 = re.sub("\(.*?\)", "", texts2)
        Summary = texts3.replace(")", "").replace("(", "").replace("=", "")
        return Summary
    except:
        return quary