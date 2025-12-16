class Fields:
    """ Class for handling the json file containing referencce types  """

    reference_types = [
    {
        "name": "article",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "journal", "required": True},
            {"name": "year", "required": True},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "pages", "required": False},
            {"name": "month", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "book",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "publisher", "required": True},
            {"name": "year", "required": True},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "address", "required": False},
            {"name": "edition", "required": False},
            {"name": "month", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "booklet",
        "fields": [
            {"name": "title", "required": True},
            {"name": "author", "required": False},
            {"name": "howpublished", "required": False},
            {"name": "address", "required": False},
            {"name": "month", "required": False},
            {"name": "year", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "conference",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "booktitle", "required": False},
            {"name": "year", "required": False},
            {"name": "editor", "required": False},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "pages", "required": False},
            {"name": "month", "required": False},
            {"name": "address", "required": False},
            {"name": "organization", "required": False},
            {"name": "publisher", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "inbook",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "chapter", "required": True},
            {"name": "publisher", "required": True},
            {"name": "year", "required": True},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "type", "required": False},
            {"name": "address", "required": False},
            {"name": "edition", "required": False},
            {"name": "month", "required": False},
            {"name": "pages", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "incollection",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "booktitle", "required": True},
            {"name": "publisher", "required": False},
            {"name": "year", "required": False},
            {"name": "editor", "required": False},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "type", "required": False},
            {"name": "chapter", "required": False},
            {"name": "pages", "required": False},
            {"name": "edition", "required": False},
            {"name": "month", "required": False},
            {"name": "address", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "inproceedings",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "booktitle", "required": False},
            {"name": "year", "required": False},
            {"name": "editor", "required": False},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "pages", "required": False},
            {"name": "month", "required": False},
            {"name": "address", "required": False},
            {"name": "organization", "required": False},
            {"name": "publisher", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "manual",
        "fields": [
            {"name": "title", "required": True},
            {"name": "author", "required": False},
            {"name": "organization", "required": False},
            {"name": "address", "required": False},
            {"name": "edition", "required": False},
            {"name": "month", "required": False},
            {"name": "year", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "mastersthesis",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "school", "required": True},
            {"name": "year", "required": True},
            {"name": "type", "required": False},
            {"name": "address", "required": False},
            {"name": "month", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "phdthesis",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "school", "required": True},
            {"name": "year", "required": True},
            {"name": "type", "required": False},
            {"name": "address", "required": False},
            {"name": "month", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "proceedngs",
        "fields": [
            {"name": "title", "required": True},
            {"name": "year", "required": True},
            {"name": "booktitle", "required": False},
            {"name": "editor", "required": False},
            {"name": "volume", "required": False},
            {"name": "number", "required": False},
            {"name": "series", "required": False},
            {"name": "address", "required": False},
            {"name": "month", "required": False},
            {"name": "organization", "required": False},
            {"name": "publisher", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "teachreport",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "institution", "required": True},
            {"name": "year", "required": True},
            {"name": "type", "required": False},
            {"name": "number", "required": False},
            {"name": "address", "required": False},
            {"name": "month", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "unpublished",
        "fields": [
            {"name": "author", "required": True},
            {"name": "title", "required": True},
            {"name": "note", "required": False},
            {"name": "month", "required": False},
            {"name": "year", "required": False},
            {"name": "annote", "required": False},
        ],
    },
    {
        "name": "misc",
        "fields": [
            {"name": "author", "required": False},
            {"name": "title", "required": False},
            {"name": "howpublished", "required": False},
            {"name": "month", "required": False},
            {"name": "year", "required": False},
            {"name": "note", "required": False},
            {"name": "annote", "required": False},
        ],
    },
]

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
        fields = set()
        for ref in self.reference_types:
            if ref['name'] == name.lower():
                for field in ref['fields']:
                    fields.add(field['name'])
        return fields

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
