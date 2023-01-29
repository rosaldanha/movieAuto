from typing import List

class Video:
    def __init__(self, title, guid):
        self.title = title
        self.guid  = guid

class Show(Video):
    def __init__(self,title,guid,episodes:List[Video]):
        super().__init__(title=title,guid=guid)
        self.episodes = episodes or []

