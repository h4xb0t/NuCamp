#!/usr/bin/env python
from pathlib import Path

# in this example, pathlib converts these individual parts of the path into the proper syntax per OS (i.e. \ for windows and / for linux-mac)
Path("spam", "bacon", "eggs")

# will print `spam\bacon\eggs`` on windows
print(str(Path("spam", "bacon", "eggs")))
