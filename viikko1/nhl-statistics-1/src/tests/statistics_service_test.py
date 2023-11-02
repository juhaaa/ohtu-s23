import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player(self):
        result = self.stats.search("Semenko")
        
        # Etsitään Semenkoa joka on listalla, tarkistetaan löytyykö.
        self.assertEqual(result.name, "Semenko")

    def test_search_player_ei_pelaajaa(self):
        result = self.stats.search("Messier")
        
        # Etsitään "Messier", joka ei ole listalla, pitäisi palauttaa None.
        self.assertEqual(result, None)

    def test_team(self):
        result = self.stats.team("EDM")

        # Joukkueen Edmonton Oilers pelaajia on 3
        self.assertEqual(len(result), 3)

    def test_top_pisteet(self):
        result = self.stats.top(4, SortBy.POINTS)
        
        # Eniten pisteitä Gretzky
        self.assertEqual(result[0].name, "Gretzky")
    
    def test_top_maalit(self):
        result = self.stats.top(4, SortBy.GOALS)
        
        # Eniten maaleja Lemieux
        self.assertEqual(result[0].name, "Lemieux")

    def test_top_syottopisteet(self):
        result = self.stats.top(4, SortBy.ASSISTS)
        
        # Eniten syöttöjä Gretzky
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_ei_tilastoa(self):
        result = self.stats.top(4, 5)
        
        # Eniten syöttöjä Gretzky
        self.assertEqual(result, None)

