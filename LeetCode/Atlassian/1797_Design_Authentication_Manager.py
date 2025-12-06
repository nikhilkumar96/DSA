from header import *

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.manager = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.manager[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        token = self.manager.get(tokenId)
        if token and token > currentTime:
            self.manager[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, value in self.manager.items():
            if value > currentTime:
                count += 1
        return count

a = ["AuthenticationManager","renew","generate","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens"]
b = [[5],["aaa",1],["aaa",2],[6],["bbb",7],["aaa",8],["bbb",10],[15]]
obj = AuthenticationManager(b[0][0])

func_call_with_two_lists(a,b,obj)