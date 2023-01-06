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



pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)



terrains = Namespace(
        FOREST = "forest",
        WATER = "water",
        OCEAN = "ocean",
        PLAINS = "plains",
        MOUNTAINS = "moutains"
)


__modes = Namespace(
    SELECTMODE = "Select Mode",
    CHANGETERRAIN = "Change tiles",
    BANANA = "banana"
)

gameoverlay = Namespace(
    modes = __modes,
    modesImages = Namespace(**{
        __modes.SELECTMODE: font.render("SELECT", True, (255,255,255)),
        __modes.CHANGETERRAIN: font.render("TILES", True, (255,255,255)),
        __modes.BANANA: font.render("BANANA", True, (255,255,255))
    })
)

"""
fillings is a helper dict, where all one should specify either an surface or color for each tile
"""
fillings = {
        terrains.FOREST: (34, 139, 34),
        terrains.WATER: (156, 211, 219),
        terrains.OCEAN: (43, 101, 236),
        terrains.PLAINS: (82, 161, 123),
        terrains.MOUNTAINS: (85, 65, 36)
}

"""
Note that surfaces can be in any size to prevent lossy compresion
"""
terrainImages = Namespace()

for tile in fillings:
    if type(fillings[tile]) == pygame.Surface:
        terrainImages[tile] = fillings[tile]
        continue

    surface = pygame.Surface((100,100))
    surface.fill(fillings[tile])
    terrainImages[tile] = surface

del(fillings)
