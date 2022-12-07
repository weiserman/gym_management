# Copyright (c) 2022, Agile.co.za and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ClassTypes(Document):
	# set a route automatically if not set by user
	def before_save(self):
		if not self.route:
			self.route = f"/class-types/{self.name}"
