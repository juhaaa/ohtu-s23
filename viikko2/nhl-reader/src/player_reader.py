import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.player_list = []
        self.response = requests.get(self.url).json()
        self.construct_players()


    def construct_players(self):
        for player_dict in self.response:
            player = Player(player_dict)
            self.player_list.append(player)