import pkg_resources
import json
from os.path import abspath, exists

DATA = abspath(pkg_resources.resource_filename(__name__, "data/marc_schema.json"))

print(exists(DATA))

DATA = json.load(open(DATA, 'r'))

