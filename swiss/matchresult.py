WIN = 0
LOSS = 1
TIE = 2


class InvalidResultError(Exception):
    pass


class MatchResult:
    def __init__(self, main_result=None):
        if not isinstance(main_result, int):
            raise InvalidResultError()
        self.main_result = main_result


class MtgMatchResult(MatchResult):
    def __init__(self, main_result=None, score=None):
        super(MatchResult, self).__init__(main_result)
        if (not isinstance(score, tuple)) or len(score) != 3:
            raise InvalidResultError()
        self.score = score


class WhMatchResult(MatchResult):
    def __init(self, main_result=None, score=None):
        super(MatchResult, self).__init__(main_result)
        if (not isinstance(score, tuple)) or len(score) != 2:
            raise InvalidResultError()
        self.score = score
