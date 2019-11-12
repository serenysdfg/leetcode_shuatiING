#简单
class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=[]
        address=list(address)
        for i in  range(len(address)):
            if address[i]=='.':
                a.append('[.]')
            else:
                a.append( address[i])
        return ''.join(i for i in a)