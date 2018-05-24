
# MarcFieldLookup

This library is intended to allow developers to build applications that allow users to explore the MARC schema more effectively.

There are two ways to explore the schema:

- by subfield using the MarcSubfieldSearch class
- by field using the MarcFieldSearch class

In addition, a developer can get the code and label and all subfields of a particular MARC field with the MarcField class

## Examples

```python
>> from marclookup.lookup import MarcField
>> mf = MarcField(field='245')
>> mf.field
'245'
>> mf.subfields
[<class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>, <class 'marclookup.lookup.subfield'>]
>> a_subfield = mf_subfields[1]
>> a_subfield.code
'b'
>> a_subfield.label
'Remainder of title'
```

```python
>> from marclookup.lookup import MarcFieldSearch
>> field_search = MarcFieldSearch(partial_phrase='Title')
>> for n in field_search:
>>      print(n)
field_search_result(marc_field='243', marc_field_label='Collective Uniform Title')
field_search_result(marc_field='630', marc_field_label='Subject Added Entry - Uniform Title')
field_search_result(marc_field='740', marc_field_label='Added Entry - Uncontrolled Related/Analytical Title')
field_search_result(marc_field='246', marc_field_label='Varying Form of Title')
field_search_result(marc_field='247', marc_field_label='Former Title')
field_search_result(marc_field='730', marc_field_label='Added Entry - Uniform Title')
field_search_result(marc_field='130', marc_field_label='Main Entry - Uniform Title')
field_search_result(marc_field='210', marc_field_label='Abbreviated Title')
field_search_result(marc_field='240', marc_field_label='Uniform Title')
field_search_result(marc_field='245', marc_field_label='Title Statement')
field_search_result(marc_field='830', marc_field_label='Series Added Entry - Uniform Title')
field_search_result(marc_field='440', marc_field_label='Series Statement/Added Entry-Title')
field_search_result(marc_field='222', marc_field_label='Key Title')
field_search_result(marc_field='242', marc_field_label='Translation of Title by Cataloging Agency')
field_search_result(marc_field='547', marc_field_label='Former Title Complexity Note')
```

```python
>> from marclookup.lookup import MarcSubFieldSearch
>> subfield_search = MarcSubFieldSearch(partial_phrase='Subject')
>> for n in subfield_search:
>>      print(n)
subfield_search_result(marc_field='072', marc_field_label='Subject Category Code', subfield_code='x', subfield_label='Subject category code subdivision')
subfield_search_result(marc_field='072', marc_field_label='Subject Category Code', subfield_code='a', subfield_label='Subject category code')
```

## Contract for Search Result Data

Every object that is in the results of MarcFieldSearch will have the following properties:

- marc_field
- marc_field_label

The results of a MarcSubFieldSearch have those properties as well as the following:

- subfield_code
- subfield_label

## Contract for subfields from MarcField.subfields

Every subfield in a given MarcField instance has the following properties:

- code
- label

## Credit

- Thanks to [pkiraly](https://github.com/pkiraly) for the [JSON schema of the marc structure](https://raw.githubusercontent.com/pkiraly/metadata-qa-marc/master/src/main/resources/marc-schema.json)

