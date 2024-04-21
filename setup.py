import json
import os

version_txt = os.path.join(os.curdir, "version.txt")

version = 1.0

data = {
    "version": version
}

with open(version_txt, mode="w") as file:
    file.write(json.dumps(data))

print("Done.")