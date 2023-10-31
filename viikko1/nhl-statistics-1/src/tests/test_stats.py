import unittest
from statistics_service import StatisticsService, SortBy
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
    def compare(self, expected, result):
        self.assertEqual(expected[0].points, result[0].points)
        self.assertEqual(expected[0].name, result[0].name)
        self.assertEqual(expected[0].team, result[0].team)

    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_top(self):
        expected = [Player("Gretzky", "EDM", 35, 89)]
        result = self.stats.top(0)
        self.compare(expected, result)

    def test_top_goals(self):
        expected = [Player("Lemieux", "PIT", 45, 54)]
        result = self.stats.top(0, SortBy.GOALS)
        self.compare(expected, result)

    def test_top_assists(self):
        expected = [Player("Gretzky", "EDM", 35, 89)]
        result = self.stats.top(0, SortBy.ASSISTS)
        self.compare(expected, result)

    def test_top_invalid(self):
        self.assertRaises(ValueError, self.stats.top, 0, "GOALS")

    def test_team(self):
        expected = [Player("Lemieux", "PIT", 45, 54)]
        result = self.stats.team("PIT")
        self.compare(expected, result)
    
    def test_search_ok(self):
        expected = [Player("Kurri",   "EDM", 37, 53)]
        result = [self.stats.search("Kurri")]
        self.compare(expected, result)

    def test_search_fail(self):
        self.assertIsNone(self.stats.search("AAAAA"))