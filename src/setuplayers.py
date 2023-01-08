from components import SettingsManager
from layers import Layer, LayerBuilder, OverlayLayers, MoveLayer, GameControl, TerrainLayer

class SetupLayers:
    def __init__(self, screenSize: tuple[int], settings: SettingsManager):
        self.root = OverlayLayers(screenSize, settings, [])
        self.root.addLayer(
                MoveLayer.builder(
                        GameControl.builder(),
                        self.getGameControlPosition
                )
        )

        gameScreen = MoveLayer.builder(
                OverlayLayers.builder(
                    [
                        TerrainLayer.builder()
                    ]
                ),
                self.getGamePosition
        )
        self.root.addLayer(gameScreen)

    def getRoot(self):
        return self.root
    
    def getGamePosition(self, screenSize, settings):
        return (
                0,
                0,
                screenSize[0],
                screenSize[1] - settings["gameControlHeight"]
        )

    def getGameControlPosition(self, screenSize, settings):
        print(screenSize)
        print(settings)
        return (
                0,
                screenSize[1] - settings["gameControlHeight"],
                screenSize[0],
                settings["gameControlHeight"],
        )

