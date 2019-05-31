class Player:
    def __init__(self, name=None, info=None):
        self.name = name
        self.info = info or {}
        self.match_results = []
        self.had_bye = False
