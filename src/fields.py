import json

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
