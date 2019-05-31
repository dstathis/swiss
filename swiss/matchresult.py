# Swiss - Swiss Tournament Software
# Copyright (C) 2019 Dylan Stephano-Shachter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

WIN = 0
LOSS = 1
TIE = 2


class InvalidResultError(Exception):
    pass


class MatchResult:
    """A base class for match results"""
    def __init__(self, main_result=None):
        if not isinstance(main_result, int):
            raise InvalidResultError()
        self.main_result = main_result


class MtgMatchResult(MatchResult):
    """An MTG style match result"""
    def __init__(self, main_result=None, score=None):
        super(MatchResult, self).__init__(main_result)
        if (not isinstance(score, tuple)) or len(score) != 3:
            raise InvalidResultError()
        self.score = score


class WhMatchResult(MatchResult):
    """A 40k style match result"""
    def __init__(self, main_result=None, score=None):
        super(MatchResult, self).__init__(main_result)
        if (not isinstance(score, tuple)) or len(score) != 2:
            raise InvalidResultError()
        self.score = score
