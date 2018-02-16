class FestivalResultModel:
    def __init__(self, name, artists, similarity):
        self.name = name
        self.artists = artists
        self.similarity = similarity

    def __eq__(self, other):
        return len(self.similarity) == len(other.similarity)

    def __lt__(self, other):
        return len(self.similarity) < len(other.similarity)
