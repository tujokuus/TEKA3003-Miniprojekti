'''
This file provides methods for handling the content (a.k.a references) of bibtex files
'''

import json
import bibtexparser # type: ignore
import requests

class Fields:
    """ Class for handling the json file containing referencce types  """

    def __init__(self):
        """ Read reference types from refs.json file """
        try:
            with open('refs.json', 'r',encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Error: file 'refs.json' not found.")
        self.reference_types = data['Reference_types']

    def get_required(self, name):
        """Gets all required fields of a reference type by name"""
        required = set()
        for ref in self.reference_types:
            if ref['name'] == name.lower():
                for field in ref['fields']:
                    if field['required'] is True:
                        required.add(field['name'])
        return sorted(required)

    def get_optional(self, name):
        """Gets all optional fields of a reference type by name"""
        optional = set()
        for ref in self.reference_types:
            if ref['name'] == name.lower():
                for field in ref['fields']:
                    if field['required'] is False:
                        optional.add(field['name'])
        return sorted(optional)

    def get_fields(self, name):
        """Gets all fields of a reference type by name"""
        for ref in self.reference_types:
            if ref['name'] == name.lower():
                return ref['fields']
        return None

    def get_ref_names(self):
        """Gets names of all reference types"""
        names = set()
        for ref in self.reference_types:
            names.add(ref['name'])
        return names

    def get_uniq_attrs(self):
        "Get names of all unique attributes"
        attrs = set()
        for ref in self.reference_types:
            for field in ref['fields']:
                if field['name'] not in attrs:
                    attrs.add(field['name'])
        return attrs

class Entry:
    """ Class representing a single entry (a.k.a reference) in bib file  """

    def __init__(self, identifier, reference_type):
        self.reference_type = reference_type
        self.identifier = identifier
        self.values: dict[str, str] = {}
        self.current_iterator_index = 0

    def add_value(self, value_type, value):
        """Assigns given value to wanted value type (a.k.a field)"""
        self.values[value_type] = value

    def remove_value(self, value_type):
        """Removes value assigned to wanted value type" (a.k.a field)"""
        self.values.pop(value_type)

    def get_value(self, value_type):
        """Returns the value of wanted value type (a.k.a field)"""
        return self.values[value_type]

    def get_value_types(self):
        """Returns a list of all value types contained in this entry"""
        return self.values.keys()

    def get_identifier(self):
        """Returns the identifier of this entry"""
        return self.identifier

    def set_identifier(self, identifier):
        """Sets wanted identifier as this entry's identifier"""
        self.identifier = identifier

    def __str__(self):
        """Outputs formatted bibtex"""
        ret = f"@{self.reference_type}{{{self.identifier},\n"
        for index, (key, value) in enumerate(self.values.items()):
            comma = ""
            if index != len(self.values) - 1:
                comma = ","
            ret += f"    {key} = {{{value}}}{comma}\n"
        ret += "}"
        return ret


class Bibtex:
    """Class for handling the entries in bibtex file"""

    def __init__(self):
        self.entries: list[Entry] = []
        self.current_iterator_index = 0

    def __iter__(self):
        self.current_iterator_index = 0
        return self

    def __next__(self):
        try:
            ret = self.entries[self.current_iterator_index]
            self.current_iterator_index += 1
            return ret
        except IndexError as exc:
            raise StopIteration from exc

    def add(self, entry):
        """Adds an entry (a.k.a reference) to list of all entries in bibtex file"""
        self.entries.append(entry)

    def add_doi(self, doi):
        """Adds an entry (a.k.a reference) to list of all entries in bibtex file by doi"""
        url = ""
        baseurl = "https://doi.org/"
        if doi.startswith("https"):
            url = doi
        elif doi.startswith("doi:"):
            url = baseurl + doi[4:]
        else:
            url = baseurl + doi
        req = requests.get(url, timeout=10, headers={"Accept": "text/bibliography; style=bibtex"})
        req.encoding = 'utf-8'
        if req.status_code != 200:
            raise FileNotFoundError
        bib_string = req.text
        self.read(bib_string)

    def remove(self, identifier):
        """Removes an entry (a.k.a reference) with matching identifier"""
        for entry in self.entries:
            if entry.get_identifier() == identifier:
                self.entries.remove(entry)

    def get(self, identifier):
        """Returns an entry (a.k.a reference) with matching identifier"""
        for entry in self.entries:
            if entry.get_identifier() == identifier:
                return entry
        return None

    def read(self, bib_string):
        """Parses entries (a.k.a references) from a bibtex string to entries"""
        library = bibtexparser.parse_string(bib_string)

        for parsed_entry in library.entries:
            entry = None
            entry = Entry(parsed_entry.key, parsed_entry.entry_type)
            for field in parsed_entry.fields:
                entry.add_value(field.key, field.value)
            self.entries.append(entry)

    def search(self, search_term: str, value_type: str | None = None):
        """
        Searches for entries by value type and its value.
        The search term is not case sensitive.
        If value type is omitted or set to None, the search term is searched from all values.

        Returns a list of found entries.
        """
        found = []
        processed_search_term = search_term.strip().lower()
        for entry in self.entries:
            if value_type is None:
                for value_type2 in entry.get_value_types():
                    if processed_search_term in entry.get_value(value_type2).lower():
                        found.append(entry)
                        break
                continue
            try:
                if processed_search_term in entry.get_value(value_type).lower():
                    found.append(entry)
            except KeyError as _exc:
                continue
        return found

    def sort(self, value_type: str, desc: bool = False):
        """
        Sorts entires based on value_type and returns them in a list.
        If an entry has no value for given value_type, it will get sorted last, in no defined order,
        even if sorting in descending order.
        The sort is in ascending order by default, but this can be changed by argument `desc`.
        """

        with_value_type = []
        without_value_type = []
        for entry in self.entries:
            try:
                entry.get_value(value_type)
                with_value_type.append(entry)
            except KeyError as _exc:
                without_value_type.append(entry)

        def key(entry):
            return entry.get_value(value_type).strip().lower()
        sorted_entries = sorted(with_value_type, key=key , reverse=desc)

        return sorted_entries + without_value_type

    def __str__(self):
        r = ""
        length = len(self.entries)
        for index, entry in enumerate(self.entries):
            r += str(entry)
            if index != length - 1:
                r += "\n\n"
        return r
