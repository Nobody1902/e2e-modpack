import json
import os

version_txt = os.path.join(os.curdir, "version.txt")

version = 1.0
minecraft_version = "1.12.2-forge-14.23.5.2860"

data = {
    "version": version,
    "minecraft_version": minecraft_version
}

with open(version_txt, mode="w") as file:
    file.write(json.dumps(data))

print("Done.")