# Minecraft-World-API
# PROJECT IS IN UNSTABLE TESTING PHASE, USAGE NOT RECOMMENDED.

This straightforward API allows you to see data about the world and players in Minecraft single-player.

# Usage

First, you can import the API by doing the following:

```python
from playerapi import PlayerAPI
player = PlayerAPI()
```

You can find what (block or entity) is player looking at by doing the following:


```python
looking_at = player.is_looking_at()
```

Or if the player will fall next move in chosen direction:
```python
# checking if player will fall on X-axis
will_fall_x = player.will_fall(True, False)
# checking if player will fall on Z-axis
will_fall_z = player.will_fall(False, True)
```
Find items in the player's inventory:

```python
inventory = player.inventory
```

Get all blocks near the player in chosen radius:

```python
blocks = player.near_blocks(radius=20)
```
Or, if you want a specific block:
```python
blocks = player.near_blocks(radius=20, block_type="stone")
```

Get all entities in the current chunk:
```python
mobs_in_chunk = player.chunk_mobs
```

And lastly, you can find basic info about the player like this:
```python
rotation = player.rotation
position = player.coords
entity = player.player_entity # returns nbt representation of player entity
```

More coming soon...
