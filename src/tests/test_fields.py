import unittest
import fields

class TestFields(unittest.TestCase):

    def setUp(self):
        self.fields = fields.Fields()

    def test_get_required(self):
        expected = ['author', 'journal', 'title', 'year']
        actual = self.fields.get_required('article')
        self.assertEqual(expected,actual)

    def test_get_required_none(self):
        expected = []
        actual = self.fields.get_required('not in ref types')
        self.assertEqual(expected,actual)

    def test_get_optional(self):
        expected = ['annote', 'month', 'note', 'year']
        actual = self.fields.get_optional('unpublished')
        self.assertEqual(expected,actual)

    def test_get_optional_none(self):
        expected = []
        actual = self.fields.get_optional('not in ref types')
        self.assertEqual(expected,actual)

    def test_get_fields(self):
        expected = {'author','title','school','year','type','address','month','note','annote'}
        actual = self.fields.get_fields('phdthesis')
        self.assertEqual(expected,actual)
    
    def test_get_fields_none(self):
        expected = set()
        actual = self.fields.get_fields('not in ref types')
        self.assertEqual(expected,actual)

    def test_get_ref_names(self):
        expected = {"article","book","booklet","conference",
        "inbook","incollection","inproceedings","manual","mastersthesis",
        "phdthesis","proceedngs","teachreport","unpublished","misc"}
        actual = self.fields.get_ref_names()
        self.assertEqual(expected,actual)

    def test_get_uniq_attrs(self):
        expected = {'month','booktitle','institution','journal','pages',
        'title','publisher','school','address','note','annote','howpublished',
        'volume','chapter','author','editor','type','number','year',
        'series','edition','organization'}
        actual = self.fields.get_uniq_attrs()
        self.assertEqual(expected,actual)
