
"""classes for performing MARC Field creation from label lookups
"""

from collections import namedtuple
import json
import pkgutil

from . import DATA as LOOKUP

class MarcField:
    """a class for finding a particular MARC field and its related subfields

    Usage:
        mf = MarcField(field='245')
        print(mf.field)
        print(mf.label)
    
    """
    def __init__(self, field=None, field_label=None):
        """instantiates an instance of the class

        KWArgs
            field (str): a string corresponding to a MARC field number. Ex: 245, 856, 600.
            field_label (str): a string corresponding to a label for a MARC field. Example: Title Statement

        Returns:
            MarcField. An instance of the MarcField class.
        """
        if field:
            self.field, self.label,\
             self.subfields = self._find_matching_field_by_code(field)
        elif field_label:
            self.field, self.label,\
             self.subfields = self._find_matching_field_by_label(field_label)

    def _find_matching_field_by_code(self, code):
        field, label = None, None
        subfields = []    
        for n_field in LOOKUP["fields"]:
            if n_field == code:
                subfields = self._find_all_subfields(n_field, LOOKUP['fields'][n_field]['subfields'])
                label = LOOKUP['fields'][n_field]['label']
                field = n_field
        return field, label, subfields

    def _find_matching_field_by_label(self, inputted_label):
        for n_field in LOOKUP["fields"]:
            if LOOKUP["fields"][n_field].get("label") == inputted_label:
                field = n_field
                label = LOOKUP["fields"][n_field]["label"]
                subfields = self._find_all_subfields(n_field, LOOKUP["fields"][n_field]["subfields"])
        return field, label, subfields

    def _find_all_subfields(self, n_field, subfields):
        output = []
        for subfield in subfields:
            subf_dict = LOOKUP["fields"][n_field]["subfields"][subfield]
            subfield_record = namedtuple('subfield', ['code', 'label'])
            subfield_record(subfield, subf_dict.get("label"))
            output.append(subfield_record)
        return output

class MarcFieldSearch:
    """a class to search for MARC fields matching a particular label string

    Usage: 
        field_search = MarcFieldSearch(field_label="Title Statement")
        for field in field_search:
            ...
            # do something

     Search results are objects with the following properties:
   
    - marc_field
    - marc_field_label
    """
    def __init__(self, field_label=None, partial_phrase=None):
        """instantiates an instance of the class

        KWArgs
            field_label (str): a string matching exactly 1 MARC field label
            partial_phrase (str): a string that may be in 1 or MARC field labels

        Returns:
            MarcFieldSearch. An instance of the MarcFieldSearch class.
        """
 
        self.field_options = self._find_all_fields(field_label, partial_phrase)

    def __iter__(self):
        for result in self.field_options:
            yield result

    def __str__(self):
        output = "Results:\n"
        for n_result in self:
            output += "{} {}\n".format(n_result.marc_field, n_result.marc_field_label)
        return output

    def _find_all_fields(self, field_label, partial_phrase):
        field_options = []
        if field_label:
           for n_field in LOOKUP["fields"]:
               if LOOKUP["fields"][n_field].get("label") and LOOKUP["fields"][n_field]["label"].lower() == field_label.lower():
                        field_info = namedtuple("field_search_result", ["marc_field", "marc_field_label"])
                        a_result = field_info(marc_field=n_field,
                                              marc_field_label=LOOKUP["fields"][n_field].get("label"))
                        field_options.append(a_result)
        else:
               for n_field in LOOKUP["fields"]:
                    if LOOKUP["fields"][n_field].get("label") and partial_phrase.lower() in LOOKUP["fields"][n_field]["label"].lower():
                        field_info = namedtuple("field_search_result", ["marc_field", "marc_field_label"])
                        a_result = field_info(marc_field=n_field,
                                              marc_field_label=LOOKUP["fields"][n_field].get("label"))
                        field_options.append(a_result)
 
        return field_options
 

class MarcSubFieldSearch:
    """a class to search for MARC subfields matching a particular label string

    Usage: 
        subfield_search = MarcSubfieldSearch(field_label="Linkage")
        for subfield in subfield_search:
            ...
            # do something

    Search results are objects with the following properties:
   
    - marc_field
    - marc_field_label
    - subfield_code
    - subfield_label
    """
    def __init__(self, field_label=None, partial_phrase=None):
        """instantiates an instance of the class

        KWArgs
            field_label (str): a string matching exactly 1 MARC subfield label
            partial_phrase (str): a string that may be in 1 or MARC subfield labels

        Returns:
            MarcSubFieldSearch. An instance of the MarcSubFieldSearch class.
        """
 
        self.subfield_options = self._find_subfield_options(field_label, partial_phrase)

    def __iter__(self):
        for item in self.subfield_options:
            yield item

    def __str__(self):
        output = "Results:\n"
        for n_result in self:
            output += "{} {}\n\t{} {}\n".format(n_result.marc_field, n_result.marc_field_label, 
                                             n_result.subfield_code, n_result.subfield_label)
        return output
   
    def _find_subfield_options(self, field_label, partial_phrase):
        subfield_options = []
        if field_label:
           for n_field in LOOKUP["fields"]:
                for subfield in LOOKUP["fields"][n_field].get("subfields", []):
                    subf_dict = LOOKUP["fields"][n_field]["subfields"][subfield]
                    if subf_dict["label"].lower() == field_label.lower():
                        field_info = namedtuple("subfield_search_result", ["marc_field", "marc_field_label", "subfield_code", "subfield_label"])
                        a_result = field_info(marc_field=n_field,
                                              marc_field_label=LOOKUP["fields"][n_field].get("label"),
                                              subfield_code=subfield,
                                              subfield_label=subf_dict.get("label"))
                        subfield_options.append(a_result)
        elif partial_phrase:
           for n_field in LOOKUP["fields"]:
                for subfield in LOOKUP["fields"][n_field].get("subfields", []):
                    subf_dict = LOOKUP["fields"][n_field]["subfields"][subfield]
                    if partial_phrase.lower() in subf_dict["label"].lower():
                        field_info = namedtuple("subfield_search_result", ["marc_field", "marc_field_label", "subfield_code", "subfield_label"])
                        a_result = field_info(marc_field=n_field,
                                              marc_field_label=LOOKUP["fields"][n_field].get("label"),
                                              subfield_code=subfield,
                                              subfield_label=subf_dict.get("label"))
                        subfield_options.append(a_result)
 
        return subfield_options
 