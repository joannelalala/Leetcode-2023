'''
referred to https://youtu.be/ZMdBEJX3gog

'''
class Solution:
    def arrangeWords(self, text: str) -> str:
        
        arr = []
        
        for index, x in enumerate(text.split()):
            arr.append((len(x), index, x.lower()))
            
        r = [x[2] for x in sorted(arr)]
        
        r[0] = r[0][0].upper()+r[0][1:]
        
        return " ".join(r)
        
        
