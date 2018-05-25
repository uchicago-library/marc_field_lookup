import pkg_resources
import json
from os.path import abspath, exists

DATA = abspath(pkg_resources.resource_filename(__name__, "marc-schema.json"))
DATA = json.load(open(DATA, 'r', encoding="utf-8"))
