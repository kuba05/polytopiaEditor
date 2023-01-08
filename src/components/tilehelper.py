import math

def getTileLength(surfaceSize, sideLength):
    """
    returns tile length given the size of display surface and the number of tiles per side
    """
    return math.floor(min(
            surfaceSize[0] / sideLength,
            #in this projection, the y axis is scaled down by the factor of 2
            surfaceSize[1] / sideLength * 2
    ) / 4) * 4

def getPositionOfTile(x, y, tileLength, sideLength):
    """
    returns coordinates of tile's left-most point, provided the map is fit so that tile (0,0) touches the line x=0 and tile (0,sideLength) touches the line y=0
    """
    
    # for each increase in x, the tile moves (tileLength/2, tileLength/4)
    # for each increase in y, the tile moves (tileLength/2, -tileLength/4)
    return (
            round((x + y) * tileLength/2),
            round((x - y + sideLength) * tileLength/4)
    )

def getTileFromCoordinates(X, Y, tileLength, sideLength):
    # let point A be the left most poinst of tile (0,0)
    # then for each point B, vector AB can ve writen as follows:
    # AB = xf + yg
    # where f = (T/2, T/4) and g = (T/2, -T/4)

    A = getPositionOfTile(0, 0, tileLength, sideLength)
    AB = (X - A[0], Y - A[1])
    f = (AB[0] / (tileLength / 2) + AB[1] / (tileLength / 4)) / 2
    g = (AB[0] / (tileLength / 2) - AB[1] / (tileLength / 4)) / 2

    return (f, g)
