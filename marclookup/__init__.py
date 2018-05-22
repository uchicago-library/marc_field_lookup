import pkgutil
import json

DATA = json.loads(pkgutil.get_data("marclookup", "data/marc-schema.json").decode("utf-8"))

#LOOKUP = json.load(pkgutil.get_data('marclookup', "data/marc.json"))["fields"]
