
"""
O = Mur
. = porte
U = sortie
X = Robot
"""

from game.gmap import TileType, Gmap


class Builder:
    TILES_DEFINITION = {
        'O': TileType.WALL,
        '.': TileType.DOOR,
        'X': TileType.ROBOT,
        'U': TileType.EXIT,
        ' ': TileType.FLOOR
    }

    def __init__(self, text):
        self.gmap = None
        self.text = text.split('\n')

    def start(self):
        self.create_base_map()
        self.convert_text_to_map()
        return self.gmap

    def estimate_height_and_width(self):
        width = 0
        height = 0
        for line in self.text:
            height += 1
            if len(line) > width:
                width = len(line)
        return width, height

    def create_base_map(self):
        width, height = self.estimate_height_and_width()
        self.gmap = Gmap(width, height)

    def convert_text_to_map(self):
        i = 0
        for line in self.text:
            remaining_width = self.gmap.width
            for char in line:
                tile = Builder.TILES_DEFINITION.get(char, TileType.WALL)
                if tile == TileType.ROBOT:
                    self.gmap.player_position = i
                    tile = TileType.FLOOR
                self.gmap.tiles[i] = tile
                i += 1
                remaining_width -= 1
            while remaining_width > 0:
                self.gmap.tiles[i] = TileType.WALL
                i += 1
                remaining_width -= 1
