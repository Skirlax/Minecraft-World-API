from nbt import *

import blocks
import mobs
import read_config

mb = mobs.Mobs()
bl = blocks.Blocks()
rc = read_config.ReadConfig()


class PlayerAPI:
    def __init__(self):
        self._player_path = f"{rc.read_single_value('world_folder', 'World Options')}/level.dat"

    @property
    def rotation(self) -> list:
        player_data = nbt.NBTFile(self._player_path)
        player_rotation = player_data["Data"]["Player"]["Rotation"]
        return [x.value for x in player_rotation]

    @property
    def region(self) -> str:
        x, z = self.coords[0], self.coords[2]
        region_name = f"r.{int(abs(x) // 512)}.{int(abs(z) // 512)}.mca"
        return self._player_path.replace("level.dat", f"region/{region_name}")

    @property
    def chunk(self) -> list:
        x, z = self.coords[0], self.coords[2]
        return [int(abs(x) // 16), int(abs(z) // 16)]

    @property
    def coords(self) -> list:
        nbt_file = nbt.NBTFile(self._player_path)
        coords = nbt_file["Data"]["Player"]["Pos"]
        return [x.value for x in coords]

    @property
    def player_entity(self) -> nbt.TAG_Compound:
        nbt_file = nbt.NBTFile(self._player_path)
        return nbt_file["Data"]["Player"]

    @property
    def blocks_near(self) -> list:
        return bl.blocks_near_player(self.player_entity, self.region, self.chunk, "any", radius=15)

    @property
    def mobs_near(self) -> list:
        return mb.mobs_in_chunk(self.region, self.chunk)

    @property
    def inventory(self) -> list:
        return self.player_entity["Inventory"].tags

    def is_looking_at(self) -> str:

        entity = mb.is_looking_at(self.mobs_near, self.player_entity)
        if entity:
            return entity

        for block in self.blocks_near:
            if bl.is_looking_at_block(self.player_entity, block, distance=15):
                return block["name"]

        return "minecraft:air"

    @staticmethod
    def will_fall(chunk_coords: list, region_path: str, player_coords: list, x: bool, z: bool) -> bool:
        return bl.will_fall(chunk_coords, region_path, player_coords, x, z)
