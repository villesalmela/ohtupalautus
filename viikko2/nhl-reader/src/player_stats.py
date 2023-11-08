
class PlayerStats:
    
    def __init__(self, reader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        return sorted(filter(lambda x: x.nationality == nationality,
                             self.reader.get_players()),
                             key=lambda x: x.points, reverse=True)