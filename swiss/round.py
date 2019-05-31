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

from swiss.player import Player

BYE = Player()


class Pairing:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


class Round:
    def __init__(self, players):
        self.pairings = []
        self.players = players

    def pair_round():
        pass
