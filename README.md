# Minecraft-World-API

This is a straightforward API that allows you to see data about world and player in Minecraft single-player.

# Usage

You can find what (block or entity) is player looking at by doing:

```
from playerapi import PlayerAPI
player = PlayerAPI()
looking_at = player.is_looking_at()
```
