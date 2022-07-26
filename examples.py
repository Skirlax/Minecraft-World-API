from playerapi import PlayerAPI

player = PlayerAPI()

# Getting what is player looking at.
looking_at = player.is_looking_at()

# checking if player will fall on X-axis
will_fall_x = player.will_fall(True, False)
# checking if player will fall on Z-axis
will_fall_z = player.will_fall(False, True)

# getting player's inventory
inventory = player.inventory

# Getting near blocks
blocks = player.near_blocks(radius=20)

blocks = player.near_blocks(radius=15, block_type="stone")

mobs_in_chunk = player.chunk_mobs

rotation = player.rotation
position = player.coords
entity = player.player_entity  # returns nbt representation of player entity
