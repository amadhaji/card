# Copyright (c) 2022, amadhaji@open-alt.com and Contributors
# See license.txt

import frappe
import unittest

class TestCard(unittest.TestCase):
	def setUp(self):
		self.doctype_doc = frappe.get_doc({
			"doctype":"DocType",
			"__newname": "Test Doc For Card",
			"module": "bonyan-app",
			"custom": 1,
			"fields":[{
					"fieldname": "found",
					"fieldtype": "Data",
					"in_standard_filter": 1,
				},
				{
					"fieldname": "not_found",
					"fieldtype": "Data",
					"in_standard_filter": 0,
				},
				{
					"fieldname": "with_default",
					"fieldtype": "Data",
					"in_standard_filter": 1,
					"default": "default"
				}
			]
		})
		self.doctype_doc.save()

		self.card = frappe.get_doc({
			"doctype": "Card",
			"card_name": "__Test Card",
			"doctype_card": "Test Doc For Card",
			"card_width": 1,
			"card_height": 1,
			"layout": "test",
		})
		self.card.save()


	def test_include_standard_filtres(self):
		self.assertIn("found", self.card.fields)
		self.assertIn("with_default", self.card.fields)


	def test_exclude_non_standard_filters(self):
		self.assertNotIn("not_found", self.card.fields)


	def test_include_default_value_with_field(self):
		self.assertRegex(self.card.fields, """.*["']?with_default["']?\s*:\s*['"]default['"]""")


	def tearDown(self):
		self.card.delete()
		self.doctype_doc.delete()
