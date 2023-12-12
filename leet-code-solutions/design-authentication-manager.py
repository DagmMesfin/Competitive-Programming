class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.time_to_live = timeToLive
        self.tokenid = defaultdict(int)
        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if not self.tokenid[tokenId] or self.tokenid[tokenId] <= currentTime:
            self.tokenid[tokenId] = self.time_to_live + currentTime

        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if self.tokenid[tokenId] and self.tokenid[tokenId] > currentTime:
            self.tokenid[tokenId] = currentTime + self.time_to_live
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        counter = 0
        for key,value in self.tokenid.items():
            counter += 1 if value > currentTime else 0
        return counter
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)