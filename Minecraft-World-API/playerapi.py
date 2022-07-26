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
    def chunk_mobs(self) -> list:
        return mb.mobs_in_chunk(self.region, self.chunk)

    @property
    def inventory(self) -> list:
        return self.player_entity["Inventory"].tags

    def is_looking_at(self) -> str:

        entity = mb.is_looking_at(self.chunk_mobs, self.player_entity)
        if entity:
            return entity

        for block in self.near_blocks:
            if bl.is_looking_at_block(self.player_entity, block, distance=15):
                return block["name"]

        return "minecraft:air"

    def will_fall(self,x: bool, z: bool) -> bool:
        return bl.will_fall(self.chunk,self._player_path, self.coords, x, z)

    def near_blocks(self, radius=15, block_type="any") -> list:
        return bl.blocks_near_player(self.player_entity, self.region, self.chunk, block_type, radius)
