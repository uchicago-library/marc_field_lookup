"""test cases for the marclookup library
"""

from io import StringIO
from unittest import TestCase
from marclookup.lookup import MarcField, MarcFieldSearch, MarcSubFieldSearch

class SpecTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPartialPhraseMarcFieldSearch(self):
        f = MarcFieldSearch(partial_phrase='Title')
        self.assertEqual(len(f.field_options), 15)

    def testExactLabelMarcFieldSearch(self):
        f = MarcFieldSearch(field_label='Title Statement')
        self.assertEqual(len(f.field_options), 1)
        self.assertEqual(f.field_options[0].marc_field_label, 'Title Statement')
        self.assertEqual(f.field_options[0].marc_field, '245')
        self.assertEqual(f.field_options[0]._fields, ('marc_field', 'marc_field_label'))

    def testPartialPhraseMarcSubFieldSearch(self):
        f = MarcSubFieldSearch(partial_phrase='Title')
        self.assertEqual(len(f.subfield_options), 87)

    def testExactLabelMarcSubFieldSearch(self):
        f = MarcSubFieldSearch(field_label='Linkage')
        self.assertEqual(len(f.subfield_options), 195)
        self.assertEqual(f.subfield_options[0]._fields, ('marc_field', 'marc_field_label', 'subfield_code', 'subfield_label'))

    def testMarcLookup(self):
        f = MarcField(field='245')
        self.assertEqual(f.label, 'Title Statement')
        self.assertEqual(f.field, '245')
        self.assertEqual(len(f.subfields), 12)
        self.assertEqual(f.subfields[0]._fields, ('code', 'label'))
