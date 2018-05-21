
"""classes for performing MARC Field creation from label lookups
"""

from collections import namedtuple
import json
import pkgutil

from . import LOOKUP

class MarcField:
    def __init__(self, field=None, field_label=None):
        if field:
            self.field, self.label,\
             self.subfields = self._find_matching_field_by_code(field)
        elif field_label:
            self.field, self.label,\
             self.subfields = self._find_matching_field_by_label(field_label)

    def _find_match_to_condition_in_lookup(self, key, func=lambda x: x == None):
        field, label = None, None
        subfields = []    
        for a_dict in LOOKUP:
            if func(a_dict.get(key)):
               field, label = a_dict.get("field"), a_dict.get("label")
               subfields = self._find_all_subfields(a_dict)
               break
        return field, label, subfields

    def _find_matching_field_by_code(self, code):
        return self._find_match_to_condition_in_lookup('code', func=lambda x: x == code)

    def _find_matching_field_by_label(self, inputted_label):
        return self._find_match_to_condition_in_lookup('label', func=lambda x: x == inputted_label)

    def _find_all_subfields(self, dictionary):
        output = []
        for subfield in dictionary.get("subfields"):
            subfield_record = namedtuple('subfield', ['code', 'label'])
            subfield_record(subfield.get("code"), subfield.get("label"))
            output.append(subfield_record)
        return output
