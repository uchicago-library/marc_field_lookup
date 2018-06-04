import pkg_resources
import json
from os.path import abspath, exists
from appdirs import user_data_dir
from configobj import ConfigObj
from configparser import SafeConfigParser
from appdirs import user_config_dir
from os.path import join

def transform_config(config_data):
    master = {"fields": {}}
    for field_name in config_data:
        field_key = field_name
        field_data = config_data[field_key]
        if field_data.get("subfields", None):
            new_dict = {"tag": "", "label": ""}
            subfield_data = field_data["subfields"]
            subfield_list = []
            for n in subfield_data:
                new_dict = {"tag": n, "label": subfield_data["label"]}
                subfield_list.append(new_dict)
            new_dict["tag"] = field_key
            new_dict["label"] = field_data["label"] 
            new_dict["repeatable"] = field_data["repeatable"]
            new_dict["subfields"] = subfield_list
            master["fields"][field_key] = new_dict
    return master

PARSER = SafeConfigParser()
PKG_DATA = abspath(pkg_resources.resource_filename(__name__, "marc-schema.json"))
PKG_DATA = json.load(open(PKG_DATA, 'r'))
LOCAL_DATA = {"fields": {}}

LOCAL_DATA_FOLDER = user_config_dir("marcFieldsLookup", "uchicago-library")
LOCAL_CONFIG_FILE = join(LOCAL_DATA_FOLDER, 'marc_local_fields.ini')

if exists(LOCAL_CONFIG_FILE):
    CONFIG = ConfigObj(LOCAL_CONFIG_FILE)
    LOCAL_DATA = transform_config(CONFIG)
    PKG_DATA["fields"].update(LOCAL_DATA["fields"])

DATA = PKG_DATA
DATA = abspath(pkg_resources.resource_filename(__name__, "marc-schema.json"))
DATA = json.load(open(DATA, 'r', encoding="utf-8"))
