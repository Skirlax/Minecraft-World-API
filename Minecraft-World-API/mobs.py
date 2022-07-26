from nbt import *


class Mobs:

    @staticmethod
    def mobs_in_chunk(path, chunk_coords) -> list:

        entity_region = region.RegionFile(path)
        nbt_chunk = entity_region.get_nbt(chunk_coords[0], chunk_coords[1])
        try:
            entities = nbt_chunk["Entities"]
        except KeyError:
            return []
        return [x for x in entities]

    @staticmethod
    def is_looking_at(entities, player) -> str:
        distance = 25
        for entity in entities:
            x_match = []
            z_match = []
            player_x, player_y, player_z = int(player["Pos"][0]), int(player["Pos"][1]), int(
                player["Pos"][2])

            entity_x, entity_y, entity_z = int(entity["Pos"][0]), int(entity["Pos"][1]), int(
                entity["Pos"][2])
            player_rotation_x = int(player["Rotation"][0])
            if not entity_y > player_y - 5 or not entity_y < player_y + 5:
                continue
            if player_rotation_x < 0:
                player_rotation_x += 360
            if 90 > player_rotation_x >= 0:
                x_match = [x for x in range(player_x, player_x - distance + 1, -1) if x == entity_x]
                z_match = [z for z in range(player_z, player_z + distance + 1) if z == entity_z]

            elif 180 > player_rotation_x >= 90:
                x_match = [x for x in range(player_x, player_x + distance + 1) if x == entity_x]
                z_match = [z for z in range(player_z, player_z + distance + 1) if z == entity_z]

            elif 270 > player_rotation_x >= 180:
                x_match = [x for x in range(player_x, player_x + distance + 1) if x == entity_x]
                z_match = [z for z in range(player_z, player_z - distance + 1, -1) if z == entity_z]

            elif 360 > player_rotation_x >= 270:
                x_match = [x for x in range(player_x, player_x - distance + 1, -1) if x == entity_x]
                z_match = [z for z in range(player_z, player_z - distance + 1, -1) if z == entity_z]

            if entity_x == player_x:
                x_match = [player_x]
            if entity_z == player_z:
                z_match = [player_z]
            if x_match and z_match:
                return entity["id"]
