import pkg_resources
import json

DATA = pkg_resources.resource_filename(__name__, "data/marc_schema.json")

print(DATA)
