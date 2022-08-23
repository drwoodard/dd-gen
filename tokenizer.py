import re
import string

class StringTokenizer:

    @staticmethod
    def tokenize(text: string, object: any) -> string:
        pattern = r'\{([^{}]+)\}'
        matches = re.findall(pattern, text)
        
        for match in matches:
            text = text.replace("{"+match+"}", str(getattr(object, match)))

        return text
        


