import re
import wikipedia

def Wikipedia(quary: str) -> str:
    try:
        quary: str = quary.replace("summary:", "")
        Summary = wikipedia.summary(quary, sentences=10)
        texts2 = re.sub("\[.*?\]", "", Summary)
        texts3 = re.sub("\(.*?\)", "", texts2)
        Summary = texts3.replace(")", "").replace("(", "").replace("=", "")
        return Summary
    except:
        return f"Sorry nothing match about : {quary}"