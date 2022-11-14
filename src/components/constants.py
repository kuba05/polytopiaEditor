class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

tiles = Namespace(
        FOREST = "forest",
        WATER = "water",
        OCEAN = "ocean",
        PLAINS = "plains",
        MOUTAINS = "moutains"
)

modes = Namespace(
        CHANGETILES = "Changetiles"
)
