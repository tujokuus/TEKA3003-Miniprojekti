import bibtexparser # type: ignore


class Entry:
    def __init__(self, identifier, reference_type):
        self.reference_type = reference_type
        self.identifier = identifier
        self.values: dict[str, str] = {}

    def add_value(self, value_type, value):
        self.values[value_type] = value

    def remove_value(self, value_type):
        self.values.pop(value_type)

    def get_value(self, value_type):
        return self.values[value_type]

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
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
        self.entries.append(entry)

    def remove(self, identifier):
        for entry in self.entries:
            if entry.get_identifier() == identifier:
                self.entries.remove(entry)

    def get(self, identifier):
        for entry in self.entries:
            if entry.get_identifier() == identifier:
                return entry
        return None

    def read(self, bib_string):
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
