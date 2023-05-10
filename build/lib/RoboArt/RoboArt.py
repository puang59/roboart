class roboart:
    def __init__(self): 
        self.base_url = "https://robohash.org"

    def robo(self, hash: str, set=1): 
        avatar = f"{self.base_url}/{hash}.png/?set=set{int(set)}"
        return avatar

    def monster(self, hash: str, set=2):
        avatar = f"{self.base_url}/{hash}.png/?set=set{int(set)}"
        return avatar
    
    def robohead(self, hash: str, set=3): 
        avatar = f"{self.base_url}/{hash}.png/?set=set{int(set)}"
        return avatar

    def kitten(self, hash: str, set=4): 
        avatar = f"{self.base_url}/{hash}.png/?set=set{int(set)}"
        return avatar

