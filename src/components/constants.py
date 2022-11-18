import pygame

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, item, value):
        self.__dict__[item] = value

    def __iter__(self):
        return iter(self.__dict__.values())

    def __len__(self):
        return len(self.__dict__)

tiles = Namespace(
        FOREST = "forest",
        WATER = "water",
        OCEAN = "ocean",
        PLAINS = "plains",
        MOUNTAINS = "moutains"
)

modes = Namespace(
        SELECT = "Select",
        CHANGETILES = "Change tiles"
)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

modesImages = Namespace(**{
    modes.SELECT: font.render("SELECT", True, (0,0,0)),
        modes.CHANGETILES: font.render("TILES", True, (0,0,0))
        })

"""
fillings is a helper dict, where all one should specify either an surface or color for each tile
"""
fillings = {
        tiles.FOREST: (34, 139, 34),
        tiles.WATER: (156, 211, 219),
        tiles.OCEAN: (43, 101, 236),
        tiles.PLAINS: (82, 161, 123),
        tiles.MOUNTAINS: (85, 65, 36)
}

"""
Note that surfaces can be in any size to prevent lossy compresion
"""
tilesImages = Namespace()

for tile in fillings:
    if type(fillings[tile]) == pygame.Surface:
        tilesImages[tile] = fillings[tile]
        continue

    surface = pygame.Surface((100,100))
    surface.fill(fillings[tile])
    tilesImages[tile] = surface

del(fillings)
