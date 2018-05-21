import pkgutil
import json

LOOKUP = json.loads(pkgutil.get_data('marclookup', "data/marc.json"))
