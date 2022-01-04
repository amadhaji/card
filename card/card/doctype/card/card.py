# Copyright (c) 2022, amadhaji@open-alt.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class Card(Document):
	def before_save(self):
		"""get doc_card fields which will be used as a filters in Print Cards MultiSelectDialog
		"""
		fields = frappe.get_all("DocField", fields = ["fieldname", "default"],
		 	filters = {"parent": self.doctype_card},
			or_filters = {"in_standard_filter": 1, "in_list_view": 1})

		fields = {field["fieldname"] : field["default"] for field in fields}
		self.filter_fields = json.dumps(fields)
		print("Hello")
