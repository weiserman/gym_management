# Copyright (c) 2022, Agile.co.za and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class Class(WebsiteGenerator):
    # Lets set a route based on the name of the class
	def before_save(self):
		if not self.route:
			self.route = f"/classes/{self.name}"

	def validate(self):
		self.set_class_datetime()
		
	# create a date time field based on separate entries
	def set_class_datetime(self):
		self.class_datetime = "%s %s" % (
		self.class_date,
		self.class_time or "00:00:00",)