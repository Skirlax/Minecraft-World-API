# Minecraft-World-API

This is a straightforward API that allows you to see data about world and player in Minecraft single-player.

# Usage

First, you can import the API by doing:

```python
from playerapi import PlayerAPI
player = PlayerAPI()
```

You can find what (block or entity) is player looking at by doing:


```python
looking_at = player.is_looking_at()
```

Or if player will fall next move in chosen direction:
```python
# checking if player will fall on X-axis
will_fall_x = player.will_fall(True, False)
# checking if player will fall on Z-axis
will_fall_z = player.will_fall(False, True)
```
Find items in player's inventory:

```python
inventory = player.inventory
```

Get all blocks near player in chosen radius:

```python
blocks = player.near_blocks(radius=20)
```
Or if you want a specific block:
```python
blocks = player.near_blocks(radius=20, block_type="stone")
```

Get all entities in the current chunk:
```python
mobs_in_chunk = player.chunk_mobs
```

And lastly, you can find basic info about player like this:
```python
rotation = player.rotation
position = player.coords
entity = player.player_entity # returns nbt representation of player entity
```


