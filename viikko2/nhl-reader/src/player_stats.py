class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.player_list

    def top_scorers_by_nationality(self, nationality):
        self.players.sort(key=lambda x: x.points, reverse=True)
        top_scorers = filter(lambda x: x.nationality == nationality, self.players)
        return top_scorers