class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):

        if self.player1_score == self.player2_score:
            return self.tie(self.player1_score)
        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage(self.player1_score, self.player2_score)
        
        else:
            return (self.score_to_string(self.player1_score) + "-"
                + self.score_to_string(self.player2_score))
    
    def tie(self, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
    
    def advantage(self, score1, score2):
        score_difference = score1 - score2
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def score_to_string(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        else:
            return "Deuce"
        
