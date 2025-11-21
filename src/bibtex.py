'''
This file provides methods for handling the content (a.k.a references) of bibtex files
'''

import bibtexparser # type: ignore

class Entry:
    """ Class representing a single entry (a.k.a reference) in bib file  """

    def __init__(self, identifier, reference_type):
        self.reference_type = reference_type
        self.identifier = identifier
        self.values: dict[str, str] = {}

    def add_value(self, value_type, value):
        """Assigns given value to wanted value type (a.k.a field)"""
        self.values[value_type] = value

    def remove_value(self, value_type):
        """Removes value assigned to wanted value type" (a.k.a field)"""
        self.values.pop(value_type)

    def get_value(self, value_type):
        """Returns the value of wanted value type (a.k.a field)"""
        return self.values[value_type]

    def get_identifier(self):
        """Returns the identifier of this entry"""
        return self.identifier

    def set_identifier(self, identifier):
        """Sets wanted identifier as this entry's identifier"""
        self.identifier = identifier

    def __str__(self):
        ret = f"@{self.reference_type}{{{self.identifier},\n"
        for index, (key, value) in enumerate(self.values.items()):
            comma = ""
            if index != len(self.values) - 1:
                comma = ","
            ret += f"    {key} = {{{value}}}{comma}\n"
        ret += "}"
        return ret


class Bibtex:
    """ Class for handling the entries in bibtex file"""

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

    def __str__(self):
        r = ""
        length = len(self.entries)
        for index, entry in enumerate(self.entries):
            r += str(entry)
            if index != length - 1:
                r += "\n\n"
        return r
