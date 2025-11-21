




class Entry:
    reference_type: str = ""
    identifier: str = ""
    values: dict[str, str] = {}

    def __init__(self, identifier, reference_type):
        self.reference_type = reference_type
        self.identifier = identifier

    def add_value(self, value_type, value):
        self.values[value_type] = value

    def remove_value(self, value_type):
        self.values.pop(value_type)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def __str__(self):
        ret = f"@{self.reference_type}{{{self.identifier}\n"
        for key, value in self.values.items():
            ret += f"    {key} = {{{value}}}\n"
        ret += "}"
        return ret


class Bibtex:
    entries: list[Entry] = []
    current_iterator_index = 0

    def __init__(self, _filename):
        self._read()

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

    def _read(self):
        # TODO: Read and parse provided file
        pass

    def save(self):
        # TODO: Write and parse
        pass
