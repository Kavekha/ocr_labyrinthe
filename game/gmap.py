from enum import Enum


class Directions(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3


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
    WALKABLE_TILES = [TileType.DOOR, TileType.FLOOR, TileType.EXIT]


    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [None] * width * height
        self.player_position = 0

    def is_out_of_bound(self, idx):
        if idx < 0 or idx > (self.height * self.width):
            return True
        return False

    def convert_str_dir(self, str_dir):
        directions = {
            "n": - self.width,
            "s": self.width,
            "e": 1,
            "o": -1
        }
        return directions.get(str_dir)

    def is_tile_available(self, str_dir):
        dir = self.convert_str_dir(str_dir)
        if not dir:
            print(f'[WARNING]: Direction not valid in is tile available : {str_dir}.')
            return False
        destination = self.player_position + dir
        if self.is_out_of_bound(destination):
            return False

        if self.tiles[destination] not in Gmap.WALKABLE_TILES:
            return False
        return True

    def move_player(self, str_dir):
        dir = self.convert_str_dir(str_dir)
        self.player_position = self.player_position + dir
        return True

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