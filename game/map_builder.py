
"""
O = Mur
. = porte
U = sortie
X = Robot
"""

from enum import Enum
from itertools import product


class TileType(Enum):
    WALL = 0
    DOOR = 1
    EXIT = 2
    ROBOT = 3
    FLOOR = 4


class Gmap:
    TILE_RENDERING = {
        TileType.WALL: '#',
        TileType.DOOR: '+',
        TileType.EXIT: 'U',
        TileType.FLOOR: ' '
    }

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [None] * width * height
        self.player_position = 0

    def __repr__(self):
        map_as_text = ""
        for i, tile in enumerate(self.tiles):
            if i % self.width == 0:
                map_as_text += '\n'
            if i != self.player_position:
                map_as_text += Gmap.TILE_RENDERING.get(tile, '?')
            else:
                map_as_text += '@'
        return map_as_text


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
                    tile = TileType.WALL
                self.gmap.tiles[i] = tile
                i += 1
                remaining_width -= 1
            while remaining_width > 0:
                self.gmap.tiles[i] = TileType.WALL
                i += 1
                remaining_width -= 1
