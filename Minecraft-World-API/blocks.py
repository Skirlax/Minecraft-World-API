import anvil
from nbt import *


class Blocks:

    # Takes a long time
    @staticmethod
    def blocks_near_player(player: nbt, region_path: str, chunk_coords: list, block: str, radius=25):
        x, y, z = int(player["Pos"][0].value), int(player["Pos"][1].value), int(player["Pos"][2].value)

        current_region = region.RegionFile(region_path)
        nbt_chunk = current_region.get_nbt(chunk_coords[0], chunk_coords[1])
        anvil_chunk = anvil.Chunk(nbt_chunk)
        # limits: x < 16, z < 16, y < 320
        filtered_blocks = []

        y_range = list(range(y - 5, y + radius + 1))
        for y_offset in y_range:
            for x_offset in range(16):
                for z_offset in range(16):
                    chunk_block = anvil_chunk.get_block(x_offset, y_offset, z_offset)
                    if "air" in chunk_block.name():
                        continue

                    if block in chunk_block.name() or block == "any":
                        first_chunk_x = chunk_coords[0] * 16
                        first_chunk_z = chunk_coords[1] * 16
                        x_coord = first_chunk_x + x_offset
                        z_coord = first_chunk_z + z_offset
                        filtered_blocks.append(
                            {"name": chunk_block.name(), "world_coords": (x_coord, y_offset, z_coord),
                             "distance from player": (abs(x_coord - x), abs(z_coord - z))})

        return filtered_blocks

    @staticmethod
    def is_looking_at_block(player: nbt, block: dict, distance=25):
        x_match = []
        z_match = []
        player_x, y, player_z = int(player["Pos"][0].value), int(player["Pos"][1].value), int(player["Pos"][2].value)
        player_rotation_x = int(player["Rotation"][0].value)
        block_x, block_y, block_z = block["world_coords"][0], block["world_coords"][1], block["world_coords"][2]

        if player_rotation_x < 0:
            player_rotation_x += 360

        if 90 > player_rotation_x >= 0:
            x_match = [x for x in range(player_x, player_x - distance + 1, -1) if x == block_x]
            z_match = [z for z in range(player_z, player_z + distance + 1) if z == block_z]

        elif 180 > player_rotation_x >= 90:
            x_match = [x for x in range(player_x, player_x - distance + 1, -1) if x == block_x]
            z_match = [z for z in range(player_z, player_z - distance + 1, -1) if z == block_z]

        elif 270 > player_rotation_x >= 180:
            x_match = [x for x in range(player_x - 1, player_x + distance + 1) if x == block_x]
            z_match = [z for z in range(player_z, player_z - distance + 1, -1) if z == block_z]

        elif 360 > player_rotation_x >= 270:
            x_match = [x for x in range(player_x, player_x + distance + 1) if x == block_x]
            z_match = [z for z in range(player_z, player_z + distance + 1) if z == block_z]

        if x_match and z_match and block["distance from player"][0] <= distance and block["distance from player"][
            1] <= distance:
            return True
        return False

    @staticmethod
    def is_next_to_player(block: dict):
        if block["distance from player"][0] <= 1 or block["distance from player"][1] <= 1:
            return True

    @staticmethod
    def will_fall(chunk_coords: list, region_path: str, player_coords: list, x: bool, z: bool):
        current_region = region.RegionFile(region_path)
        nbt_chunk = current_region.get_nbt(chunk_coords[0], chunk_coords[1])
        anvil_chunk = anvil.Chunk(nbt_chunk)
        if x:
            range_x = range(int(player_coords[0]) - 1, int(player_coords[0]) + 2)
            for x_coord in range_x:
                if "air" in anvil_chunk.get_block(x_coord, int(player_coords[1]), int(player_coords[2])).name():
                    return True
        elif z:
            range_z = range(int(player_coords[2]) - 1, int(player_coords[2]) + 2)
            for z_coord in range_z:
                if "air" in anvil_chunk.get_block(int(player_coords[0]), int(player_coords[1]), z_coord).name():
                    return True
        else:
            return False

        return False
