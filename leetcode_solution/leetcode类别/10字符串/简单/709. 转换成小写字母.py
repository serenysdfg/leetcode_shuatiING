class Solution:
    def toLowerCase(self, str: str) -> str:
        for i in range(len(str)):
            if str[i].isupper():
                str = str.replace(str[i], str[i].lower())
        return str
    # return str.lower()
