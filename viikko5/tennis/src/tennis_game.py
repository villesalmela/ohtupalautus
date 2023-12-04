from enum import IntEnum


class ScoreEnum(IntEnum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3
    Game = 4


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0

    def increase_score(self) -> None:
        self.score += 1


class TennisScore:
    ADVANTAGE_MARGINAL = 1
    WIN_MARGINAL = 2

    @staticmethod
    def __get_better(player1: Player, player2: Player) -> Player:
        return max(player1, player2, key=lambda x: x.score)

    @classmethod
    def get_score(cls, player1: Player, player2: Player) -> str:
        is_deuce = player1.score >= ScoreEnum.Forty and player2.score >= ScoreEnum.Forty
        is_advantage = player1.score >= ScoreEnum.Game or player2.score >= ScoreEnum.Game

        if player1.score == player2.score:
            if is_deuce:
                return "Deuce"
            else:
                return f"{ScoreEnum(player1.score).name}-All"  
        else:
            if is_advantage:
                score_diff = abs(player1.score - player2.score)
                if score_diff >= cls.WIN_MARGINAL:
                    return f"Win for {cls.__get_better(player1, player2).name}"
                elif score_diff == cls.ADVANTAGE_MARGINAL:
                    return f"Advantage {cls.__get_better(player1, player2).name}"
                else:
                    raise RuntimeError("Unexpected error")
            else:
                return f"{ScoreEnum(player1.score).name}-{ScoreEnum(player2.score).name}"


class TennisGame:
    def __init__(self, player1_name, player2_name, scoring_system=TennisScore):
        self.player_1 = Player(player1_name)
        self.player_2 = Player(player2_name)
        self.players = {player1_name: self.player_1, player2_name: self.player_2}
        self.scoring_system = scoring_system

    def won_point(self, player_name):
        self.players[player_name].increase_score()

    def get_score(self):
        return self.scoring_system.get_score(self.player_1, self.player_2)
