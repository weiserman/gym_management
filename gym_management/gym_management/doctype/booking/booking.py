# Copyright (c) 2022, Agile.co.za and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate 
from frappe.utils import today
from frappe.model.document import Document

class Booking(Document):
	pass

# check if we allow historic bookings?
@frappe.whitelist()
def check_in_past():
	past_bookings = frappe.db.get_single_value(
		"Gym Settings", "past_bookings"
	)
	if past_bookings:
		return False
	return True